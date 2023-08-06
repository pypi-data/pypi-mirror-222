import subprocess
import os, os.path
import argparse
from sed import *

AWS_ACCOUNT = os.environ.get('AWS_ACCOUNT')

def generateRootCertificate():
	if (os.path.isfile("./certs/root.ca.key") and os.path.isfile("./certs/root.ca.pem")):
		print("root certificates already exists, no need to generate them")
	else:
		# Generate root key
		proc = subprocess.run(["openssl genrsa -out ./certs/root.ca.key 2048"], shell=True, check=True, capture_output=True)
		# request certificate (signed by this root key??)
		proc = subprocess.run(["openssl req -x509 -new -nodes -key ./certs/root.ca.key -sha256 -days 1024 -out ./certs/root.ca.pem -subj \"/CN=root/C=LU/L=Luxembourg/ST=Luxembourg/O=AWS/OU=Demo\""], shell=True, check=True, capture_output=True)

def registerRootCertificate():
	## Register certificate
	# Get registration code:
	proc = subprocess.run(["aws iot get-registration-code --region ${AWS_REGION} | jq -r \'.[\"registrationCode\"]\'"], shell=True, check=True, capture_output=True)
	regCode = proc.stdout.decode("utf-8")[:-1]

	# Generate CSR
	verificationCsrCmd = "openssl req -new -key ./certs/root.ca.key -out ./certs/verificationCert.csr -subj \"/CN=" + regCode + "\""
	proc = subprocess.run([verificationCsrCmd], shell=True, check=True, capture_output=True)

	# Sign the CSR
	signCsrCmd = "openssl x509 -req -in ./certs/verificationCert.csr -CA ./certs/root.ca.pem -CAkey ./certs/root.ca.key -CAcreateserial -out ./certs/verificationCert.pem -days 500 -sha256"
	proc = subprocess.run([signCsrCmd], shell=True, check=True, capture_output=True)

	# Register self signed root certificate:
	proc = subprocess.run(["mkdir -p tmp"], shell=True, check=True, capture_output=True)
	sed_to_file('./etc/regfile.tmp', './tmp/regfile', 'AWS_ACCOUNT', AWS_ACCOUNT)
	try:
		# Certificate might already be registered, so we use try/except here
		registerCrtCmd = "aws iot register-ca-certificate --ca-certificate file://certs/root.ca.pem --verification-cert file://certs/verificationCert.pem --set-as-active  --allow-auto-registration --registration-config file://tmp/regfile --region ${AWS_REGION}"
		proc = subprocess.run([registerCrtCmd], shell=True, check=True, capture_output=True)
	except Exception as ex:
		print("Error: " + str(ex))

## Generate device private key and certificate
def generateDeviceCertificate(imei):
	genPrivKeyCmd = "openssl genrsa -out ./certs/deviceName.key 2048"
	genPrivKeyCmd = genPrivKeyCmd.replace("deviceName", imei)
	genCsrCmd = "openssl req -new -key ./certs/deviceName.key -out ./certs/deviceName.csr  -subj \"/CN=deviceName\""
	genCsrCmd = genCsrCmd.replace("deviceName", imei)
	genTempCrt = "openssl x509 -req -in ./certs/deviceName.csr -CA ./certs/root.ca.pem -CAkey ./certs/root.ca.key -CAcreateserial -out ./certs/deviceName.crt.tmp -days 500 -sha256"
	genTempCrt = genTempCrt.replace("deviceName", imei)
	# concatenateCrts = "cat ./certs/deviceName.crt.tmp ./certs/root.ca.pem > ./certs/deviceName.crt" # This was the command used in AWS sample, but it doesn't work for our device when we concatenate these two certificates
	concatenateCrts = "cat ./certs/deviceName.crt.tmp > ./certs/deviceName.crt"
	concatenateCrts = concatenateCrts.replace("deviceName", imei)

	# Generate Private key
	proc = subprocess.run([genPrivKeyCmd], shell=True, check=True, capture_output=True)

	# Generate CSR
	proc = subprocess.run([genCsrCmd], shell=True, check=True, capture_output=True)

	# Generate temporary device certificate from CSR, sign it with root.ca certificate and key
	proc = subprocess.run([genTempCrt], shell=True, check=True, capture_output=True)

	# Concatenate root.ca certificate and device temporary certificate to final device certificate (TODO: try just using temporary device certificate, why is this needed?)
	proc = subprocess.run([concatenateCrts], shell=True, check=True, capture_output=True)

	# Remove device temporary certificate and CSR (they are not needed anymore)
	proc = subprocess.run(["rm ./certs/" + imei + ".crt.tmp"], shell=True, check=True, capture_output=True)
	proc = subprocess.run(["rm ./certs/" + imei + ".csr"], shell=True, check=True, capture_output=True)

## Provision a device:
def provisionDevice(imei):
	# Get endpoint
	endpointCmd = "aws iot describe-endpoint --endpoint-type iot:Data-ATS --region ${AWS_REGION} | jq -r .endpointAddress"
	proc = subprocess.run([endpointCmd], shell=True, check=True, capture_output=True)
	print(proc.stdout)
	endpoint = proc.stdout.decode("utf-8")[:-1]

	# Publish to "/register" topic (only if connected to the internet), in order to activate the certificates
	pubCmd  = "mosquitto_pub --cafile ./certs/AmazonRootCA1.pem --cert ./certs/deviceName.crt --key ./certs/deviceName.key -h " + endpoint
	pubCmd += " -p 8883 -q 0 -i deviceName -d --tls-version tlsv1.2 -m '' -t '/register'"
	pubCmd = pubCmd.replace("deviceName", imei)
	try:
		proc = subprocess.run([pubCmd], shell=True, check=True, capture_output=True)
		print(proc.stdout)
	except Exception as ex:
		print("error: " + str(ex))

	try:
		proc = subprocess.run([pubCmd], shell=True, check=True, capture_output=True)
		print(proc.stdout)
	except Exception as ex:
		print("error: " + str(ex))

def publish(imei):
	endpointCmd = "aws iot describe-endpoint --endpoint-type iot:Data-ATS --region ${AWS_REGION} | jq -r .endpointAddress"
	proc = subprocess.run([endpointCmd], shell=True, check=True, capture_output=True)
	print(proc.stdout)
	endpoint = proc.stdout.decode("utf-8")[:-1]

	# Publish dummy message to a test topic in order to see if everything works:
	pubCmd = "mosquitto_pub -d --cafile ./certs/AmazonRootCA1.pem  --cert ./certs/deviceName.crt --key ./certs/deviceName.key -h " + endpoint
	pubCmd += " -p 8883 -q 0 -t deviceName -i deviceName --tls-version tlsv1.2 -m \"hello from python\""
	pubCmd = pubCmd.replace("deviceName", imei)
	proc = subprocess.run([pubCmd], shell=True, check=True, capture_output=True)
	print(proc.stdout)

def main(imei = "defaultDeviceName"):
	try:
		generateRootCertificate()
		registerRootCertificate()
		generateDeviceCertificate(imei)
		provisionDevice(imei)
		publish(imei)  # test publish, not needed
	except Exception as ex:
		print("error: " + str(ex))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process IMEI.')
	parser.add_argument('imei', type=str, help='an IMEI for processing', nargs='?', default='123456789')
	args = parser.parse_args()
	main(args.imei)

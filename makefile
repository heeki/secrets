include etc/execute_env.sh

cfn:
	# aws --profile ${PROFILE} cloudformation create-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --capabilities CAPABILITY_IAM | jq
	aws --profile ${PROFILE} cloudformation create-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --parameters file://etc/execute_env.json --capabilities CAPABILITY_IAM | jq

cfn.update:
	# aws --profile ${PROFILE} cloudformation update-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --capabilities CAPABILITY_IAM | jq
	aws --profile ${PROFILE} cloudformation update-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --parameters file://etc/execute_env.json --capabilities CAPABILITY_IAM | jq

exec:
	python src/secrets.py

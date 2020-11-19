include etc/execute_env.sh

cfn:
	aws --profile ${PROFILE} cloudformation create-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --parameters file://etc/execute_env.json --capabilities CAPABILITY_IAM | jq

cfn.update:
	aws --profile ${PROFILE} cloudformation update-stack --stack-name ${STACK} --template-body file://${TEMPLATE} --parameters file://etc/execute_env.json --capabilities CAPABILITY_IAM | jq

cfn.outputs:
	@KMS_KEY_ID=`aws --profile ${PROFILE} cloudformation describe-stacks --stack-name ${STACK} | jq -r '.Stacks[].Outputs[].OutputValue'` || true
	@echo "export KMS_KEY_ID=${KMS_KEY_ID}" || true
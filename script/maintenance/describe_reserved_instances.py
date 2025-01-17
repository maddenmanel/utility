import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# 创建 EC2 客户端
def get_ec2_client():
    try:
        ec2 = boto3.client('ec2')
        return ec2
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS 凭证未配置或不完整，请配置凭证！")
        exit(1)

# 获取并打印预留实例的信息
def describe_reserved_instances(ec2):
    try:
        # 获取预留实例的信息
        response = ec2.describe_reserved_instances()

        # 如果没有预留实例
        if not response['ReservedInstances']:
            print("没有找到预留实例。")
            return

        # 打印每个预留实例的ID和到期时间
        for ri in response['ReservedInstances']:
            print(f"预留实例ID: {ri['ReservedInstancesId']}, 到期时间: {ri['End']}")

    except Exception as e:
        print(f"发生错误: {e}")

# 主程序
if __name__ == "__main__":
    ec2 = get_ec2_client()  # 获取EC2客户端
    describe_reserved_instances(ec2)  # 查询预留实例信息

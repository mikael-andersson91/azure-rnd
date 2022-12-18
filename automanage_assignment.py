import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.automanage import AutomanageClient


def main():
    rg = "resourceGroupName"
    profile_name = "configurationProfileName"
    virtual_machines = "vmName1,vmName2".split(",")
    SUBSCRIPTION_ID = os.getenv('SUBSCRIPTION_ID')

    # Create Automanage Client
    credential = DefaultAzureCredential()
    client = AutomanageClient(credential, SUBSCRIPTION_ID)



    # Create custom profile assignment
    custom_profile_assignment = {
        "properties": {
            "configurationProfile": f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{rg}/providers/Microsoft.Automanage/configurationProfiles/{profile_name}"
        }
    }

    # Assign each virtual machine to automanage profile
    for vm in virtual_machines:
        # Assign vm to configuration profile assignment
        client.configuration_profile_assignments.create_or_update(
            "default", rg, vm, custom_profile_assignment)

        # Get configuration profile assignment
        assignment = client.configuration_profile_assignments.get(
            rg, "default", vm)
        print(assignment)


if __name__ == '__main__':
    main()
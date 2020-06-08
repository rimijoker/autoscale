"""To test the implementation of gcloud.py"""
import gcloud
import utils.gcloud_configurations as configs


NEW = gcloud.GoogleCloud(
    credentials="/home/rimijoker/GCP Login/terraform-gsoc.json",
    project_id="terraform-275401",
    region="us-central1",
)

# NEW.create_cluster(
#     name="my-cluster",
#     machine_type=configs.MachineType.f1_micro,
#     zone=configs.Zone.us_central1_a,
#     image_family=configs.ImageFamily.ubuntu_2004_lts,
#     target_size=3,
# )

NEW.create_budget("011AB6-83EE1B-0F96E3")

NEW.destroy()

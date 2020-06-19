"""To test the implementation of gcloud.py"""
import gcloud
import utils.gcloud_configurations as configs


NEW = gcloud.GoogleCloud(
    credentials="/home/rimijoker/GCP Login/gcp-autoscaling-org.json",
    project_id="gcp-autoscaling",
    region="us-central1",
)

# NEW.create_cluster(
#     name="my-cluster",
#     machine_type=configs.MachineType.f1_micro,
#     zone=configs.Zone.us_central1_a,
#     image_family=configs.ImageFamily.ubuntu_2004_lts,
#     target_size=3,
# )

NEW.create_budget("01EC12-68D5B3-B974BB")

NEW.destroy()

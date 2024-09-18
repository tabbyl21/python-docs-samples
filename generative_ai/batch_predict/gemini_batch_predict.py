# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.cloud.aiplatform import BatchPredictionJob


# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.cloud.aiplatform import BatchPredictionJob

import os


PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
# LOCATION = "us-central1"


def batch_prediction_gemini_example(
    input_uri: str = None, output_uri: str = None
) -> BatchPredictionJob:
    """Perform batch text prediction using a Gemini AI model.
    Args:
        input_uri (str, optional): URI of the input dataset. Could be a BigQuery table or a Google Cloud Storage file.
            E.g. "gs://[BUCKET]/[DATASET].jsonl" OR "bq://[PROJECT].[DATASET].[TABLE]"
        output_uri (str, optional): URI where the output will be stored.
            Could be a BigQuery table or a Google Cloud Storage file.
            E.g. "gs://[BUCKET]/[OUTPUT].jsonl" OR "bq://[PROJECT].[DATASET].[TABLE]"
    Returns:
        batch_prediction_job: The batch prediction job object containing details of the job.
    """=

    # [START generativeaionvertexai_batch_predict_gemini_createjob]
    from vertexai.preview.batch_prediction import BatchPredictionJob

    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = 'example_project'
    # input_uri = "bq://example_project.example_dataset.example_table"

    # Initialize vertexai
		vertexai.init(project=PROJECT, location="us-central1")
    
    # Submit a batch prediction job with Gemini model
		job = BatchPredictionJob.submit("gemini-1.5-flash-001", input_uri)

		# Check job status
		print(f"Job resouce name: {job.resource_name}")
		print(f"Model resource name with the job: {job.model_name}")
		print(f"Job state: {job.state.name}")

		# Refresh the job until complete
		while not job.has_ended:
 				time.sleep(5)
				job.refresh()

		# Check if the job succeeds
		if job.has_succeeded:
				print("Job succeeded!")
		else:
				print(f"Job failed: {job.error}")

		# Check the location of the output
		print(f"Job output location: {job.output_location}")
    # Example response:
    #     bq://example_project.gen_ai_batch_prediction.predictions_2024-09-17-11-09-45-ABC123
    # [END generativeaionvertexai_batch_predict_gemini_createjob]
    return batch_prediction_job


if __name__ == "__main__":
    batch_prediction_gemini_example()

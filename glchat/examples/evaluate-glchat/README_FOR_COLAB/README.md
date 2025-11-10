# Evaluate GLChat - Google Colab Guide

## What is This?

This guide helps you test how well **GLChat** answers questions. You'll provide test questions and see how accurately your selected application / chatbot responds. The evaluation process runs automatically in **Google Colab** (a free online tool for running code) and shows you detailed results about the chatbot's performance.

**What you'll accomplish:**
- Test the chatbot with your own questions and scenarios
- Get scores showing how well the chatbot performs
- View detailed analysis of each answer in a dashboard

## 1. Prerequisites

Before you begin, make sure you have:
- Access to Google Account (@gdplabs.id)
- Access to the [shared drive folder](https://drive.google.com/drive/u/0/folders/1per1tZBH9DDQ_0jfsIwNgFbEL5fp-JAi) (this contains configuration files needed for the evaluation)
- **Langfuse service is accessible**: Before running the evaluation, check that the Langfuse dashboard at https://langfuse.obrol.id/ can be opened (you should not see a "503 Service Temporarily Unavailable" error)

### Checking and Starting Langfuse Service

If the Langfuse URL shows "503 Service Temporarily Unavailable" or cannot be accessed, you need to turn on the Langfuse service.

**For technical users:**
- Go to the "start-stop-cloud-resources" channel in the "SRE Glair" Slack workspace (https://sreglair.slack.com)
- Execute this Slack command to turn on Langfuse:
  ```
  /turn on aws ec2 bosa-poc-langfuse 302546992452 ap-southeast-3
  ```
- To turn off Langfuse (if needed), replace "on" with "off" in the command:
  ```
  /turn off aws ec2 bosa-poc-langfuse 302546992452 ap-southeast-3
  ```
- Wait a few minutes for the service to start, then check if https://langfuse.obrol.id/ is accessible
- Langfuse will turn off automatically at 23.59 WIB. Turn on if you need to run the test after.
- Please do not turn off when you are done before the automated turn off time. Other teams may still use it.


**For non-engineers:**
- If you cannot access Langfuse, contact the evals team to turn on the service for you

## 2. Important Notes Before You Start

### Authentication During Execution

When you run the evaluation, you will encounter prompts for authentication:

**a. Google Drive Mount** (may be required)
- You may be prompted to mount your Google Drive
- This will ask you to authenticate with your Google account
- Click the URL that appears, sign in with your Google account (@gdplabs.id), and follow the authentication steps
- This allows the notebook to access files from your Google Drive

**b. Google Cloud Login (gcloud)** (may be required)
- You may see a URL asking you to authenticate with Google Cloud
- Click the URL to open it in a new tab
- Sign in with your Google account (@gdplabs.id)
- After authentication, copy from the provided URL
- Paste the URL back into the notebook cell where prompted
- Press Enter to continue
- This allows the notebook to install the private SDK module

**c. Environment Passphrase**
- You will be prompted for a passphrase (password) to decrypt the encrypted configuration file
- Enter the passphrase when prompted. If you don't know the passphrase, please ask the evals team
- The passphrase is needed to unlock the configuration settings that allow the evaluation to connect to various services

**Using Your Own Credentials (Optional)**

If you don't provide your own credentials, the evaluation will use the default credentials from the encrypted file:
- **Langfuse**: Results will be logged to the `glchat_beta` project in Langfuse
- **Google Sheets**: Uses the evals team's Google Sheets service account credentials
- **GLChat**: Uses the GLChat beta base URL and API key

If you need to use different credentials (for example, different Langfuse or GLChat settings), you can add them yourself using Colab Secrets:
- In the Colab sidebar, look for the "Secrets" section (🔑 icon)
- **You only need to add the credentials you want to customize** - any credentials you add will override the defaults, but you don't need to add all of them
- Add your credentials using these secret keys (only add the ones you want to customize):
  - `LANGFUSE_PUBLIC_KEY` - Your Langfuse public key
  - `LANGFUSE_SECRET_KEY` - Your Langfuse secret key
  - `LANGFUSE_HOST` - Your Langfuse host URL
  - `GOOGLE_SHEETS_CLIENT_EMAIL` - Your Google Sheets service account email
  - `GOOGLE_SHEETS_PRIVATE_KEY` - Your Google Sheets service account private key
  - `GLCHAT_BASE_URL` - Your GLChat base URL
  - `GLCHAT_API_KEY` - Your GLChat API key
  - `OPENAI_API_KEY` - Your OpenAI API key
  - `GOOGLE_API_KEY` - Your Google API key
- If you add credentials in Colab Secrets, they will be used instead of the values from the encrypted file

## 3. Prepare Dataset

Before evaluation, you need to prepare a Google Sheets document with all the information needed for evaluation.

### Storage Options for Your Dataset

You have two ways to store your Google Sheets:

**Option 1: Use Your Own Google Service Account** (for technical users)
- **What it is**: A Google service account is a special type of account that allows automated access to Google services. This requires technical setup.
- **What to do**: If you already have one or want to create it, you can store the Google Sheets yourself. You'll need to fill in secure credentials (called "Colab secrets") in the notebook. Look for the "Secrets" section in the Colab sidebar.

**Option 2: Use Our Shared Folder** (recommended for most users)
- **What it is**: A simple folder where you can upload your Google Sheets directly.
- **What to do**: Put your Google Sheets in our [datasets folder](https://drive.google.com/drive/u/0/folders/1hmSVTstuqNzAdzeBNmoC3XQgpFmNXJt_) on Google Drive. This is simpler and doesn't require any technical setup.

**💡 Recommendation**: If you're not sure which option to choose, use **Option 2** (shared folder). It's easier and works for most use cases.

### Dataset Requirements

Your dataset must use **standardized column names** so the system can automatically recognize and process your data correctly. The column names must match specific requirements.

**Before using the module**, please make sure your dataset columns match the required names. See the [Prepare Your Dataset](https://gdplabs.gitbook.io/sdk/tutorials/evaluation/evaluate-glchat-tutorial#step-2-prepare-your-dataset) section in our GitBook for the complete list of required column names and examples.

## 4. Prepare Attachments (Skip if You Don't Have Any)

If your evaluation includes file attachments (like images, PDFs, or documents), you'll need to upload them first.

### Storage Options for Attachments

**Option 1: Use Your Own Google Service Account** (for technical users)
- If you already have a Google service account, you can upload attachments to any folder your service account can access.
- In the Colab notebook, fill in the `attachments_google_client_email` and `attachments_google_private_key` fields in the form (look for the form in the second cell of the notebook).

**Option 2: Use Our Shared Folder** (recommended for most users)
- Create your own folder in [this Google Drive folder](https://drive.google.com/drive/u/0/folders/1lqVxajjQ3bklY7ITS82fyDDAsuQN6trq)
- Upload all your attachments there
- In the Colab notebook, put the folder ID in the `attachments_gdrive_folder_id` field in the form

**💡 Recommendation**: If you're not sure which option to choose, use **Option 2** (shared folder).

## 5. Fill the Configuration Form

In the Google Colab notebook, you'll find a form section. Fill in the following fields:

### Required Fields

- **`google_sheets_id`**: The ID of your Google Sheets document
  - **How to find it**: Look at your Google Sheets URL. It looks like: `https://docs.google.com/spreadsheets/d/15oQq2HOM02qP3_ZLm4AStB7fqAhoGlshhkOsOFXCSK8/edit`
  - The ID is the long string between `/d/` and `/edit`
  - Example: `"15oQq2HOM02qP3_ZLm4AStB7fqAhoGlshhkOsOFXCSK8"`

- **`worksheet_name`**: The name of the worksheet tab in your Google Sheets
  - **How to find it**: Look at the bottom of your Google Sheets. You'll see tabs (like "Sheet1", "Sheet2", or a custom name). Use the exact name of the tab you want to evaluate.
  - Example: `"glchat_test_data"` or `"Sheet1"`

- **`user_id`**: Your user ID
  - Example: `"tester_eval1@glair.ai"`

### Optional Fields

- **`chatbot_id`**: The chatbot ID you want to test. If you leave this empty, it will use `"general-purpose"` by default.

- **`model_name`**: The model name you want to test. If you leave this empty, it will use `"GPT 5 Mini"` by default.

- **`attachments_gdrive_folder_id`**: The Google Drive folder ID where your attachments are stored (if you have attachments)
  - **How to find it**: Look at the Google Drive folder URL. It looks like: `https://drive.google.com/drive/folders/1sY7a7yZiAfMlM0ozXlEnzb4EbN84sl2N`
  - The folder ID is the long string after `/folders/`
  - If you leave this empty, it will use `"1sY7a7yZiAfMlM0ozXlEnzb4EbN84sl2N"` by default. It is the [general](https://drive.google.com/drive/u/0/folders/1sY7a7yZiAfMlM0ozXlEnzb4EbN84sl2N) folder in the Google Drive.

- **`attachments_google_client_email`**: Your Google service account client email (only needed if using Option 1 for attachments)
  - Example: `"abc.iam.gserviceaccount.com"`

- **`attachments_google_private_key`**: Your Google service account private key (only needed if using Option 1 for attachments)
  - Example: `"abc123..."`

## 6. How to Run

1. In the Google Colab notebook, click **"Runtime"** in the top menu bar
2. Select **"Run all"** from the dropdown menu
3. Wait for the evaluation to complete

The notebook will run all cells automatically from top to bottom.

**Note:** During execution, you may encounter prompts for authentication (see section 2 above for detailed instructions).

## 7. View Your Results

After the evaluation completes, you can view your results at:

**Langfuse Dashboard** - https://langfuse.obrol.id/

**What is Langfuse?** Langfuse is a web-based dashboard where you can view and analyze your evaluation results. It shows detailed information about how well the chatbot performed.

The evaluation results will show:
- Individual scores for each query
- Overall performance metrics
- Detailed evaluation breakdowns

You can filter and analyze the results using the Langfuse interface. For more information on how to use the dashboard, see the [View Evaluation Results in Langfuse](https://gdplabs.gitbook.io/sdk/tutorials/evaluation/evaluate-glchat-tutorial#step-6-view-evaluation-results-in-langfuse) section in our GitBook.

---

## Key Terms Explained

**Google Colab**: A free online tool that lets you run code in your web browser. You don't need to install anything on your computer.

**Service Account**: A special type of Google account that allows automated access to Google services. Usually only needed for advanced technical setups.

**Colab Secrets**: A secure way to store sensitive information (like passwords or keys) in Google Colab. You can find them in the Colab sidebar under the "Secrets" section.

**gcloud**: Google Cloud Platform's command-line tool. You may need to authenticate with it when running the evaluation.

**Environment Variables**: Configuration settings needed for the evaluation to run properly (like API keys and service URLs). They're stored in an encrypted file (`.env.gpg`) that requires a passphrase to decrypt. You can also override these by adding your own credentials in Colab Secrets.

**Langfuse**: A dashboard tool that displays and analyzes your evaluation results. It's a web-based interface you can access in your browser.

**Worksheet Tab**: The individual sheets within a Google Sheets document. You can see them at the bottom of your Google Sheets as tabs (like "Sheet1", "Sheet2").

---

**Need help?** Contact the team if you encounter any issues or have questions about the evaluation process.

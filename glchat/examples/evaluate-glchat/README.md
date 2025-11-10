## ⚙️ Prerequisites

- Access to Google Account (@gdplabs.id)
- Access to the [shared drive folder](https://drive.google.com/drive/u/0/folders/1per1tZBH9DDQ_0jfsIwNgFbEL5fp-JAi)
- **Langfuse service is accessible**: Check that the Langfuse dashboard at https://langfuse.obrol.id/ can be opened (should not see a "503 Service Temporarily Unavailable" error)

## 📖 Important Note

**This README provides a quick overview only. For complete step-by-step instructions, please check the [README_FOR_COLAB](./README_FOR_COLAB/) folder.**

The `README_FOR_COLAB` folder contains two detailed guides:

- **[README_SIMPLE.md](./README_FOR_COLAB/README_SIMPLE.md)**: Recommended for **Non-Engineers** - Simple guide with no customization options, using default settings
- **[README.md](./README_FOR_COLAB/README.md)**: For users who need **customization** - Includes instructions for using custom credentials, service accounts, and advanced configurations

## 🚀 Getting Started

**Note:** This example is designed to run in **Google Colab**. Please use the Jupyter notebook (`run_evaluate_glchat.ipynb`) in Google Colab for the best experience.

1. **Open in Google Colab**

   - Upload `run_evaluate_glchat.ipynb` to Google Colab, or
   - Open the notebook directly in [this Google Colab](https://colab.research.google.com/drive/17hXNvMM3SMifpKUQfRBATTM4QRF9AG88).

2. **Prepare your dataset**

   - Create a Google Sheets document with your test questions following the required format
   - Upload your Google Sheets to the [datasets folder](https://drive.google.com/drive/u/0/folders/1hmSVTstuqNzAdzeBNmoC3XQgpFmNXJt_) on Google Drive
   - See the [Prepare Your Dataset](https://gdplabs.gitbook.io/sdk/tutorials/evaluation/evaluate-glchat-tutorial#step-2-prepare-your-dataset) section in our GitBook for the complete list of required column names

3. **Fill the configuration form**

   In the notebook, fill in the required fields:
   - `google_sheets_id`: The ID of your Google Sheets document
   - `worksheet_name`: The name of the worksheet tab
   - `user_id`: Your user ID

4. **Run the evaluation**

   - Click **"Runtime"** → **"Run all"** in the Google Colab menu
   - Follow any authentication prompts that appear (Google Drive mount, gcloud login, environment passphrase)

5. **View your results**

   After completion, view your results at the [Langfuse Dashboard](https://langfuse.obrol.id/)

## 📚 Reference

- For detailed instructions, see the [README_FOR_COLAB](./README_FOR_COLAB/) folder

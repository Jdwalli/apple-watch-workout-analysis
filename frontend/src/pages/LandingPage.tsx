import React from "react";
import { FileDropzone } from "../components/common/FileDropzone";
import { useNavigate } from "react-router-dom";
import ApiClient from "../clients/api_client";
import {
  RequestError,
  UploadExportResponse,
  ApiResponse,
} from "../types/client_types";

interface Props {}

const LandingPage: React.FC<Props> = (props: Props) => {
  const apiClient = new ApiClient();
  const [uploading, setUploading] = React.useState(false);
  const [uploadSuccess, setUploadSuccess] = React.useState(false);
  const navigate = useNavigate();

  const onFileUpload = (acceptedFiles: File[]) => {
    const zipFile = acceptedFiles[0];
    setUploading(true);
    apiClient
      .uploadExport(zipFile)
      .then((response: ApiResponse<UploadExportResponse>) => {
        setUploading(false);
        setUploadSuccess(true);
        setTimeout(() => {
          navigate("/workouts");
        }, 5000);
      })
      .catch((error) => {
        setUploading(false);
        if (error.response && error.response.status === 400) {
          const { errors } = error.response.data.uploadContext;
          const errorMessages = errors
            .map((e: RequestError) => `${e.errorMessage}`)
            .join("\n");
          alert(
            "Error(s) occurred when uploading the export:\n" + errorMessages
          );
        } else {
          alert("An unexpected error occurred.");
        }
      });
  };

  return (
    <div className="mt-32 max-w-6xl flex flex-col justify-center items-center mx-auto my-auto">
      <main>
        <section>
          <h1 className="font-bold text-white text-4xl text-center mb-2">
            Apple Watch Workout Analysis Tool
          </h1>
          <p className="text-center text-lg">
            Upload your Apple Health export file to analyze all recorded
            workouts!
          </p>
        </section>
        <section className="mt-10">
          <FileDropzone onDrop={onFileUpload} />
        </section>
        <section className="mt-2">
          {uploading && <p className="text-white">Parsing Health Export...</p>}
          {!uploading && uploadSuccess && (
            <p className="text-white">
              Upload successful! Redirecting in 5 seconds...
            </p>
          )}
        </section>
      </main>
    </div>
  );
};

export default LandingPage;

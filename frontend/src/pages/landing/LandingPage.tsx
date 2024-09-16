import React from "react";
import { FileDropzone } from "@/components/FileDropzone";
import ApiClient from "@/clients/api_clients";

const LandingPage: React.FC = () => {
  const apiClient = new ApiClient();
  const [uploading, setUploading] = React.useState(false);
  const [fileName, setFileName] = React.useState("");

  const onFileUpload = (acceptedFiles: File[]) => {
    const zipFile = acceptedFiles[0];
    setUploading(true);
    apiClient
      .uploadExport(zipFile)
      .then((data) => {
        setUploading(false);
      })
      .catch((error) => {
        setUploading(false);
        if (error.response && error.response.status === 400) {
          alert("This is not an Apple Health Export!");
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
        <section>
          <p>
            {" "}
            {uploading ? <p className="text-white">Uploading...</p> : null}
          </p>
        </section>
      </main>
    </div>
  );
};

export default LandingPage;

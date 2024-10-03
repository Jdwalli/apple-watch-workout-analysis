import React from "react";
import { FileDropzone } from "@/components/FileDropzone";
import ApiClient from "@/clients/api_clients";
import { useSelector, useDispatch } from "react-redux";
import { updateExportUploadingStatus } from "@/redux/features/exportUploadingStatusSlice";
import { RootState } from "@/redux/store";
import { useNavigate } from "react-router-dom";

const LandingPage: React.FC = () => {
  const apiClient = new ApiClient();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const exportUploadingStatus = useSelector(
    (state: RootState) => state.exportUploadingStatus.exportUploadingStatus
  );

  const onFileUpload = (acceptedFiles: File[]) => {
    const zipFile = acceptedFiles[0];
    dispatch(updateExportUploadingStatus(true));
    apiClient
      .uploadExport(zipFile)
      .then(() => {
        dispatch(updateExportUploadingStatus(false));
        navigate("/workouts");
      })
      .catch((error) => {
        dispatch(updateExportUploadingStatus(false));
        if (error.response && error.response.status === 400) {
          alert("This is not an Apple Health Export!");
        }
      });
  };

  return (
    <div className="mt-32 max-w-6xl flex flex-col justify-center items-center mx-auto my-auto">
      <main>
        <section>
          <h1 className="font-bold text-4xl text-center mb-2">
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
          <p> {exportUploadingStatus ? <p>Uploading...</p> : null}</p>
        </section>
      </main>
    </div>
  );
};

export default LandingPage;

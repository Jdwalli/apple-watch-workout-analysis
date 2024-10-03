import React from "react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { FileDropzone } from "./FileDropzone";
import { Button } from "@/components/ui/button";
import { useSelector, useDispatch } from "react-redux";
import { updateExportUploadingStatus } from "@/redux/features/exportUploadingStatusSlice";
import { RootState } from "@/redux/store";
import ApiClient from "@/clients/api_clients";
import { useNavigate } from "react-router-dom";

const UploadButtonDialog: React.FC = () => {
  const navigate = useNavigate();
  const apiClient = new ApiClient();
  const dispatch = useDispatch();
  const [isOpen, setIsOpen] = React.useState(false);
  const [disabled, setDisabled] = React.useState(false);

  const exportUploadingStatus = useSelector(
    (state: RootState) => state.exportUploadingStatus.exportUploadingStatus
  );

  React.useEffect(() => {
    setDisabled(exportUploadingStatus);
  }, [exportUploadingStatus]);

  const onFileUpload = (acceptedFiles: File[]) => {
    const zipFile = acceptedFiles[0];
    dispatch(updateExportUploadingStatus(true));
    navigate("/");
    setIsOpen(exportUploadingStatus);
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
    <AlertDialog open={isOpen}>
      <AlertDialogTrigger asChild>
        <Button onClick={() => setIsOpen(true)} disabled={disabled}>
          Upload
        </Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Upload a new Apple Health Export</AlertDialogTitle>
          <AlertDialogDescription>
            <FileDropzone onDrop={onFileUpload} />
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogAction onClick={() => setIsOpen(false)}>
            Close
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
};

export default UploadButtonDialog;

import React from "react";
import { useDropzone } from "react-dropzone";
import { useSelector } from "react-redux";
import { RootState } from "@/redux/store";

interface WrapperProps {
  onDrop: (files: File[]) => void;
}

const baseStyle = {
  flex: 1,
  display: "flex",
  flexDirection: "column" as const,
  alignItems: "center",
  padding: "3rem",
  borderWidth: 2,
  borderRadius: 5,
  borderStyle: "dashed",
  outline: "none",
  transition: "border .24s ease-in-out",
};

const focusedStyle = { borderColor: "#1E94FA" };
const acceptStyle = { borderColor: "#04E204" };
const rejectStyle = { borderColor: "#FF3B30" };

const FileDropzone: React.FunctionComponent<WrapperProps> = (
  props: WrapperProps
) => {
  const [disabled, setDisabled] = React.useState(false);

  const exportUploadingStatus = useSelector(
    (state: RootState) => state.exportUploadingStatus.exportUploadingStatus
  );

  React.useEffect(() => {
    setDisabled(exportUploadingStatus);
  }, [exportUploadingStatus]);

  const {
    getRootProps,
    getInputProps,
    isFocused,
    isDragAccept,
    isDragReject,
    open,
  } = useDropzone({
    onDrop: props.onDrop,
    useFsAccessApi: false,
    multiple: false,
    accept: {
      "application/zip": [".zip"],
      "application/x-7z-compressed": [".7z"],
      "application/gzip": [".gz"],
    },
    onError: (e: Error) => console.error(`File Dropzone Error: ${e}`),
  });

  const style = React.useMemo(
    () => ({
      ...baseStyle,
      ...(isFocused ? focusedStyle : {}),
      ...(isDragAccept ? acceptStyle : {}),
      ...(isDragReject ? rejectStyle : {}),
    }),
    [isFocused, isDragAccept, isDragReject]
  );

  return (
    <div
      className="p-3"
      {...getRootProps({ style })}
      onClick={(e) => e.stopPropagation()}
    >
      <input {...getInputProps()} disabled={disabled} />
      <p>
        {disabled
          ? "File upload is disabled."
          : "Drag 'n' drop apple health export zip file here, or click to select file"}
      </p>
      <button
        className="inline-block rounded text-base font-bold leading-[1.2] cursor-pointer mx-0 my-2 px-4 py-2 border-2 border-solid"
        type="button"
        onClick={open}
        disabled={disabled}
      >
        Open File Dialog
      </button>
      <em>(Only an Apple Health Export zip file will be accepted)</em>
    </div>
  );
};

export { FileDropzone };

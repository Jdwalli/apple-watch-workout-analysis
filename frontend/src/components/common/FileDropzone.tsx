import React, { FunctionComponent, useMemo } from "react";
import { useDropzone } from "react-dropzone";

interface WrapperProps {
  onDrop: (files: File[]) => void;
}

const baseStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column' as const,
    alignItems: 'center',
    padding: '3rem',
    borderWidth: 2,
    borderRadius: 5,
    borderColor: '#eeeeee',
    borderStyle: 'dashed',
    color: '#bdbdbd',
    outline: 'none',
    transition: 'border .24s ease-in-out'
};

const focusedStyle = { borderColor: "#1E94FA" };
const acceptStyle = { borderColor: "#04E204" };
const rejectStyle = { borderColor: "#FF3B30" };

const FileDropzone: FunctionComponent<WrapperProps> = (props: WrapperProps) => {
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
    onError: (e: any) => console.error(`File Dropzone Error: ${e}`),
  });


  const style = useMemo(
    () => ({
      ...baseStyle,
      ...(isFocused ? focusedStyle : {}),
      ...(isDragAccept ? acceptStyle : {}),
      ...(isDragReject ? rejectStyle : {}),
    }),
    [isFocused, isDragAccept, isDragReject]
  );

  return (
      <div className="p-3" {...getRootProps({ style })} onClick={e => e.stopPropagation()}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop apple health export zip file here, or click to select file</p>
        <button className="inline-block text-green bg-[black] rounded text-base font-bold leading-[1.2] cursor-pointer mx-0 my-2 px-4 py-2 border-2 border-solid border-green" type="button" onClick={open}>
          Open File Dialog
        </button>
        <em>(Only an Apple Health Export zip file will be accepted)</em>
      </div>
  );
};

export { FileDropzone };
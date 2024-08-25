export interface ApiClientRequest {
  httpMethod: "GET" | "POST";
  path: string;
  body?: any;
  queryParams?: any;
  headers?: any;
}

export interface ApiResponse<T> {
  data: T;
}

export interface UploadError {
  errorCode: number;
  errorMessage: string;
}

interface UploadContext {
  statusCode: number;
  processingTime: number;
  uploadStartTime: number;
  uploadEndTime: number;
  errors: UploadError[];
}

export interface UploadExportResponse {
  uploadContext: UploadContext;
}

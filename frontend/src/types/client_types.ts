import { WorkoutContext, WorkoutDetailsContext } from "./workout_types";


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

// Upload Context Interface
export interface RequestError {
  errorCode: number;
  errorMessage: string;
}

interface UploadContext {
  statusCode: number;
  processingTime: number;
  uploadStartTime: number;
  uploadEndTime: number;
  errors: RequestError[];
}

export interface GetWorkoutsByDateParameters {
  workoutStartDate: string;
}

export interface ExportStatusContext {
  statusCode: number;
  exportPresent: boolean;
  errors: RequestError[];
}

// API Responses

// /api/upload response
export interface UploadExportResponse {
  uploadContext: UploadContext;
}

// /api/export-status response
export interface ExportStatusResponse {
  exportStatusContext: ExportStatusContext;
}

// /api/workout response
export interface WorkoutResponse {
  workoutContext: WorkoutContext;
}

// /api/workout-details response
export interface WorkoutDetailsResponse {
  workoutDetailsContext: WorkoutDetailsContext;
}

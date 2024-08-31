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


// Workout Context Interface 
export interface WorkoutMetadata {
  workoutLocationType: string;
  averageMETs: number;
  weatherTemperature: number;
  weatherHumidity: number;
  timeZone: string;
  maximumSpeed: number;
  averageSpeed: number;
  physicalEffortEstimationType: string;
  elevationAscended: number;
  elevationDescended: number;
  swimmingLocationType: string;
  swimmingStrokeStyle: string;
  lapLength: number;
  swolfScore: number;
  waterSalinity: number;
}

export interface WorkoutVitals {
  heartRate: {
    chart: Record<string, string[]>;
    unit: string;
  };
}

export interface WorkoutStatistics {
  heartRate: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
  };
  activeEnergyBurned: {
    sum: number;
    unit: string;
  };
  basalEnergyBurned: {
    sum: number;
    unit: string;
  };
  distanceWalkingRunning: {
    sum: number;
    unit: string;
  };
  stepCount: {
    sum: number;
    unit: string;
  };
  runningGroundContactTime: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: Record<string, string[]>;
  };
  runningPower: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: Record<string, string[]>;
  };
  runningVerticalOscillation: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: Record<string, string[]>;
  };
  runningSpeed: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: Record<string, string[]>;
  };
  runningStrideLength: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: Record<string, string[]>;
  };
  distanceSwimming: {
    sum: number;
    unit: string;
  };
  swimmingStrokeCount: {
    sum: number;
    unit: string;
  };
}

export interface WorkoutStats {
  workoutName: string;
  workoutDuration: number;
  workoutDurationUnit: string;
  workoutTotalDistance: number;
  workoutTotalDistanceUnit: string;
  workoutTotalEnergyBurned: number;
  workoutTotalEnergyBurnedUnit: string;
  workoutCreationDate: string;
  workoutStartDate: string;
  workoutEndDate: string;
  workoutStatistics: WorkoutStatistics;
  workoutMetadata: WorkoutMetadata;
  workoutRoute: string;
  workoutVitals: WorkoutVitals;
}

export interface WorkoutContext {
  statusCode: number;
  requestedDate: string;
  workouts: WorkoutStats[];
  errors: RequestError[];
}

// API Responses

// /api/upload response
export interface UploadExportResponse {
  uploadContext: UploadContext;
}

// /api/workout response
export interface WorkoutResponse {
  workoutContext: WorkoutContext;
}

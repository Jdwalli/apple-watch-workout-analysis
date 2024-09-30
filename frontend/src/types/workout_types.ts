import { RequestError } from "./client_types";

export type WorkoutLocationTypes = "Unknown" | "Indoor" | "Outdoor";

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
    chart: {
      time: string[];
      value: number[];
    };
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
    chart: {
      time: string[];
      value: number[];
    };
  };
  runningPower: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: {
      time: string[];
      value: number[];
    };
  };
  runningVerticalOscillation: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: {
      time: string[];
      value: number[];
    };
  };
  runningSpeed: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: {
      time: string[];
      value: number[];
    };
  };
  runningStrideLength: {
    average: number;
    minimum: number;
    maximum: number;
    unit: string;
    chart: {
      time: string[];
      value: number[];
    };
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
  workoutDeviceName: string;
  workoutStartDate: string;
  workoutEndDate: string;
  workoutStatistics: WorkoutStatistics;
  workoutMetadata: WorkoutMetadata;
  workoutRoute: WorkoutRoute;
  workoutVitals: WorkoutVitals;
}

export interface WorkoutRoute {
  course: number[];
  elevation: number[];
  hAcc: number[];
  vAcc: number[];
  latitude: number[];
  longitude: number[];
  speed: number[];
  time: string[];
}

export interface WorkoutContext {
  statusCode: number;
  requestedDate: string;
  workouts: WorkoutStats[];
  errors: RequestError[];
}

export interface WorkoutDetailsContext {
  statusCode: number;
  totalWorkouts: number;
  workoutDates: string[];
  errors: RequestError[];
}

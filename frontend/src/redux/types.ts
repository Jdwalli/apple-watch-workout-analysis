import { WorkoutStats } from "@/types/workout_types";

export interface SelectedWorkoutDate {
  selectedWorkoutDate: string | undefined;
}

export interface ExportUploadingStatus {
  exportUploadingStatus: boolean;
}

export interface SelectedWorkout {
  workout: WorkoutStats | undefined;
}

export interface ExportDataStatus {
  exportDataStatus: boolean;
}

export interface WorkoutLoadingStatus {
  workoutLoadingStatus: boolean;
}

export interface RootState {
  selectedWorkoutDate: SelectedWorkoutDate;
}

export interface Action {
  type: string;
  payload: any;
}

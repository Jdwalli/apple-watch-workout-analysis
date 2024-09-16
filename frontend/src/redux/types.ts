
export interface SelectedWorkoutDate {
  selectedWorkoutDate: string | undefined 
}

export interface RootState {
  selectedWorkout: SelectedWorkoutDate
  
}

export interface Action {
  type: string;
  payload: any;
}
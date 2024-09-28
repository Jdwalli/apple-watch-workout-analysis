import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { WorkoutStats } from "@/types/workout_types";

interface SelectedWorkout {
  workout: WorkoutStats | undefined;
}

const initialWorkoutState: SelectedWorkout = {
  workout: undefined,
};

export const selectedWorkoutSlice = createSlice({
  name: "selectedWorkout",
  initialState: initialWorkoutState,
  reducers: {
    updateSelectedWorkout: (
      state,
      action: PayloadAction<{ workout: WorkoutStats | undefined }>
    ) => {
      state.workout = action.payload.workout;
    },
    resetSelectedWorkout: (state) => {
      state.workout = undefined;
    },
  },
});

export const { updateSelectedWorkout, resetSelectedWorkout } =
  selectedWorkoutSlice.actions;

export default selectedWorkoutSlice.reducer;

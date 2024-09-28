import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { WorkoutLoadingStatus } from "../types";

const initialState: WorkoutLoadingStatus = {
  workoutLoadingStatus: false,
};

export const workoutLoadingStatusSlice = createSlice({
  name: "workoutLoadingStatus",
  initialState: initialState,
  reducers: {
    updateWorkoutLoadingStatus: (state, action: PayloadAction<boolean>) => {
      state.workoutLoadingStatus = action.payload;
    },

    resetWorkoutLoadingStatus: (state) => {
      state.workoutLoadingStatus = false;
    },
  },
});

export const { updateWorkoutLoadingStatus, resetWorkoutLoadingStatus } =
  workoutLoadingStatusSlice.actions;

export default workoutLoadingStatusSlice.reducer;

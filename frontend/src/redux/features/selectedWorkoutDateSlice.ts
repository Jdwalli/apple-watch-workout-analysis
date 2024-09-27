import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { SelectedWorkoutDate } from "../types";

const initialState: SelectedWorkoutDate = {
  selectedWorkoutDate: undefined,
};

export const selectedWorkoutDateSlice = createSlice({
  name: "selectedWorkoutDate",
  initialState: initialState,
  reducers: {
    updateSelectedWorkoutDate: (
      state,
      action: PayloadAction<{ data: SelectedWorkoutDate }>
    ) => {
      state.selectedWorkoutDate = action.payload.data.selectedWorkoutDate;
    },

    resetSelectedWorkoutDate: (state) => {
      state.selectedWorkoutDate = undefined;
    },
  },
});

export const { updateSelectedWorkoutDate, resetSelectedWorkoutDate } =
  selectedWorkoutDateSlice.actions;

export default selectedWorkoutDateSlice.reducer;

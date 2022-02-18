import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../app/store";

export interface AppState {
  csrfTokenExp: boolean;
}
const initialState: AppState = {
  
  csrfTokenExp: false,
};
export const appSlice = createSlice({
  name: "app",
  initialState,
  reducers: {
    toggleCsrfState: (state) => {
      state.csrfTokenExp = !state.csrfTokenExp;
    },
  },
});
export const { toggleCsrfState } =
  appSlice.actions;

export const selectCsrfState = (state: RootState) => state.app.csrfTokenExp;
export default appSlice.reducer;
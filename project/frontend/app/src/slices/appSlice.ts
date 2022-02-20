import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../app/store";

export interface AppState {
  csrfTokenExp: boolean;
  email: string;
}
const initialState: AppState = {
  csrfTokenExp: false,
  email: "",
};
export const appSlice = createSlice({
  name: "app",
  initialState,
  reducers: {
    toggleCsrfState: (state) => {
      state.csrfTokenExp = !state.csrfTokenExp;
    },
    setEmail: (state, action) => {
      state.email = action.payload;
    },
  },
});
export const { toggleCsrfState, setEmail } = appSlice.actions;

export const selectCsrfState = (state: RootState) => state.app.csrfTokenExp;
export const selectEmail = (state: RootState) => state.app.email;

export default appSlice.reducer;

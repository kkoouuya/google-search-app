import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import appReducer from "../slices/appSlice";
import siteReducer from "../slices/siteSlice";

export const store = configureStore({
  reducer: {
    app: appReducer,
    site: siteReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;

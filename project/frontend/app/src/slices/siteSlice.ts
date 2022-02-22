import axios from "axios";
import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../app/store";
import { PostSite, SiteBase, PostFavoSite } from "../types/SiteType";


export type SiteState = {
  siteList: PostSite[];
  favoSiteList: SiteBase[];
  word: string;
};

export interface ErrorResponse {
  message: any;
}

const initialState: SiteState = {
  siteList: [],
  favoSiteList: [],
  word: "",
};

export const serachSite = createAsyncThunk<
  PostSite[],
  string,
  { rejectValue: ErrorResponse }
>("sites/searchSite", async (word, thunkAPI) => {
  try {
    console.log("searchSite発動");
    const res = await axios.post(
      `${process.env.REACT_APP_API_URL}/scrape/?keyword=${word}`
    );
    return res.data;
  } catch (err) {
    thunkAPI.rejectWithValue({ message: err });
    throw err;
  }
});

export const createFavoSite = createAsyncThunk<
  SiteBase,
  PostFavoSite,
  { rejectValue: ErrorResponse }
>("sites/faveSite", async (site, thunkAPI) => {
  try {
    const res = await axios.post(`${process.env.REACT_APP_API_URL}/favorite/`);
    return res.data;
  } catch (err) {
    thunkAPI.rejectWithValue({ message: err });
    throw err;
  }
});

export const siteSlice = createSlice({
  name: "site",
  initialState,
  reducers: {
    setWord: (state, action: PayloadAction<string>) => {
      state.word = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(serachSite.fulfilled, (state, action) => {
      state.siteList = action.payload;
      console.log(state.siteList);
      state.word = "";
    });
    builder.addCase(createFavoSite.fulfilled, (state, action) => {
      state.favoSiteList.push(action.payload);
    });
  },
});

export const { setWord } = siteSlice.actions;
export const selectSiteListState = (state: RootState) => state.site.siteList;
export const selectWord = (state: RootState) => state.site.word;

export default siteSlice.reducer;

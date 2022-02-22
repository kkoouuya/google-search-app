import axios from "axios";
import { useQuery } from "react-query";
import { useHistory } from "react-router-dom";
import { setEmail } from "../slices/appSlice"
import {useAppDispatch} from "../app/hooks"
import { GetUserInfo } from "../types/AuthType";

axios.defaults.withCredentials = true;

export const useQueryUser = () => {
  const dispatch = useAppDispatch()
  const history = useHistory();
  const getCurrentUser = async () => {
    const { data } = await axios.get<GetUserInfo>(
      `${process.env.REACT_APP_API_URL}/user`
    );
    dispatch(setEmail(data.message))
    return data;
  };
  return useQuery({
    queryKey: "user",
    queryFn: getCurrentUser,
    staleTime: Infinity,
    onError: () => history.push("/"),
  });
};
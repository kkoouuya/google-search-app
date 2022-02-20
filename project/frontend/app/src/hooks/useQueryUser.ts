import { useQuery } from "react-query";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { GetUserInfo } from "../types/AuthType";
import { selectEmail } from "../slices/appSlice"
import {useAppSelector} from "../app/hooks"

axios.defaults.withCredentials = true;

export const useQueryUser = () => {
  const email = useAppSelector(selectEmail)
  const history = useHistory();
  const getCurrentUser = async () => {
    const { data } = await axios.get<GetUserInfo>(
      `${process.env.REACT_APP_API_URL}/user`
    );
    return data;
  };
  return useQuery({
    queryKey: "user",
    queryFn: getCurrentUser,
    staleTime: Infinity,
    onError: () => history.push("/"),
  });
};
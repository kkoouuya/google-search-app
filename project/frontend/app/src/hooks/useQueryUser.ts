import { useQuery } from "react-query";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Email } from "../types/AuthType";
axios.defaults.withCredentials = true;


export const useQueryUser = () => {
  const history = useHistory();
  const getCurrentUser = async () => {
    const { data } = await axios.get<Email>(
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
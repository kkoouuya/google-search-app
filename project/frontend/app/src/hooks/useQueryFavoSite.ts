import axios from "axios";
import { useQuery } from "react-query";
import { useHistory } from "react-router-dom";
import { toggleCsrfState } from "../slices/appSlice";
import { useAppDispatch } from "../app/hooks";
import { SiteBase } from "../types/SiteType";

axios.defaults.withCredentials = true;

export const useQueryFavoSite = () => {
  const dispatch = useAppDispatch();
  const history = useHistory();

  const getFavoSite = async () => {
    const { data } = await axios.get<SiteBase[]>(
      `${process.env.REACT_APP_API_URL}/favorite/`
    );
    return data
  }
  return useQuery({
    queryKey: ["favosite"],
    queryFn: () => getFavoSite(),
    staleTime: Infinity,
    onError: (err: any) => {
      alert(`${err.response.data.detail}\n${err.message}`);
      if (
        err.response.data.detail === "The JWT has expired" ||
        err.response.data.detail === "The CSRF token has expired."
      ) {
        dispatch(toggleCsrfState());
        history.push("/");
      }
    },
  });
}
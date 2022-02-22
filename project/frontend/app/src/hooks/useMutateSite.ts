import axios from "axios";
import { useHistory } from "react-router-dom";
import { useQueryClient, useMutation } from "react-query";
import { useAppDispatch } from "../app/hooks";
import { toggleCsrfState } from "../slices/appSlice";
import { PostFavoSite, SiteBase } from "../types/SiteType";

export const useMutateSite = () => {
  const history = useHistory();
  const dispatch = useAppDispatch();
  const queryClient = useQueryClient();

  const createFavoSiteMutation = useMutation(
    async (postSite: PostFavoSite) =>
      await axios.post(
        `${process.env.REACT_APP_API_URL}/register/favosite`,
        postSite,
        { withCredentials: true }
      ),
    {
      onSuccess: (res) => {
        const previousFavoSite =
          queryClient.getQueryData<SiteBase[]>("favosite");
        if (previousFavoSite) {
          queryClient.setQueryData("favosite", [
            ...previousFavoSite,
            res.data,
          ]);
        }
      },
      onError: (err: any) => {
        alert(`${err.response.data.detail}\n${err.message}`);
        if (err.response.data.detail === "The CSRF token has expired.") {
          dispatch(toggleCsrfState());
          history.push("/");
        }
      },
    }
  );

  const putFavoSiteMutation = useMutation(
    (site_id: string) =>
      axios.put<SiteBase>(
        `${process.env.REACT_APP_API_URL}/favorite/${site_id}`,
        {},
        { withCredentials: true }
      ),
    {
      onSuccess: (res) => {
        queryClient.setQueryData("favosite", res.data)
      },
      onError: (err: any) => {
        alert(`${err.response.data.detail}\n${err.message}`);
        if (err.response.data.detail === "The CSRF token has expired.") {
          dispatch(toggleCsrfState());
          history.push("/");
        }
      },
    }
  );

  return { createFavoSiteMutation, putFavoSiteMutation };
};

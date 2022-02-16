import axios from "axios";
import { useHistory } from "react-router-dom";
import { useMutation } from "react-query";
import { useAppDispatch } from "../app/hooks";
import { toggleCsrfState } from "../slices/appSlice";
import { Credentials } from "../types/AuthType";

export const useMutateAuth = () => {
  const history = useHistory();
  const dispatch = useAppDispatch();

  const loginMutation = useMutation(
    async (user: Credentials) =>
      await axios.post(`${process.env.REACT_APP_API_URL}/login`, user, {
        withCredentials: true,
      }),
    {
      onSuccess: () => {
        history.push("/site");
      },
      onError: (err: any) => {
        alert(`${err.response.data.detail}\n${err.message}`);
        if (err.response.data.detail === "The CSRF token has expired.") {
          dispatch(toggleCsrfState());
        }
      },
    }
  );

  const registerMutation = useMutation(
    async (user: Credentials) =>
      await axios.post(`${process.env.REACT_APP_API_URL}/register`, user),
    {
      onError: (err: any) => {
        alert(`${err.response.data.detail}\n${err.message}`);
        if (err.response.data.detail === "The CSRF token has expired.") {
          dispatch(toggleCsrfState());
        }
      },
    }
  );

  const logoutMutation = useMutation(
    async () =>
      await axios.post(
        `${process.env.REACT_APP_API_URL}/logout`,
        {},
        {
          withCredentials: true,
        }
      ),
    {
      onSuccess: () => {
        history.push("/");
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

  return { loginMutation, registerMutation, logoutMutation };
};

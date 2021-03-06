import { useEffect } from "react";
import axios from "axios";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { CsrfToken } from "./types/AuthType";
import { useAppSelector } from "./app/hooks";
import { selectCsrfState } from "./slices/appSlice";
import { Auth } from "./components/Auth";
import { Site } from "./components/Site";

function App() {
  const csrf = useAppSelector(selectCsrfState);

  useEffect(() => {
    const getCsrfToken = async () => {
      const res = await axios.get<CsrfToken>(
        `${process.env.REACT_APP_API_URL}/csrftoken`
      );
      axios.defaults.headers.common["X-CSRF-Token"] = res.data.csrf_token;
      console.log(res.data.csrf_token);
    };
    getCsrfToken();
  }, [csrf]);

  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Auth />
          </Route>
          <Route exact path="/site">
            <Site />
          </Route>
        </Switch>
      </BrowserRouter>
    </>
  );
}

export default App;

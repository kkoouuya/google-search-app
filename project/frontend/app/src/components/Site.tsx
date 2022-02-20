import { useEffect, VFC } from "react";
import { LogoutIcon } from "@heroicons/react/outline";
import { NewspaperIcon } from "@heroicons/react/solid";
import { useAppSelector, useAppDispatch } from "../app/hooks";
import { useProcessAuth } from "../hooks/useProcessAuth";
import { SiteList } from "./SiteList";
import { FavoSiteList } from "./FavoSiteList";
import { selectWord, setWord, serachSite } from "../slices/siteSlice";
import { useQueryUser } from "../hooks/useQueryUser";
import { selectEmail, setEmail } from "../slices/appSlice";

export const Site: VFC = () => {
  const { logout } = useProcessAuth();
  const { data: dataUser } = useQueryUser();
  const dispatch = useAppDispatch();
  const word = useAppSelector(selectWord);
  const email = useAppSelector(selectEmail);
 
  useEffect(() => {
    dispatch(setEmail(dataUser?.message));
  }, []);

  return (
    <div className="flex justify-center items-center flex-col min-h-screen text-gray-600 font-mono">
      <div className="flex items-center">
        <NewspaperIcon className="h-8 w-8 mr-3 text-green-500" />
        <span className="text-center text-3xl font-extrabold">
          Google Search Scraping APP
        </span>
      </div>
      <p className="my-3 text-sm">{dataUser?.message}</p>
      <LogoutIcon
        onClick={logout}
        className="h-7 w-7 mt-1 mb-5 text-blue-500 cursor-pointer"
      />
      <div>
        <input
          className="mb-3 mr-3 px-3 py-2 border border-gray-300"
          placeholder="title ?"
          type="text"
          onChange={(e) => dispatch(setWord(e.target.value))}
          value={word}
        />
        <button
          className="disabled:opacity-40 mx-3 py-2 px-3 text-white bg-indigo-600 rounded mb-10"
          onClick={() => dispatch(serachSite(word))}
        >
          search
        </button>
      </div>
      <div className="mb-10">
        <SiteList />
      </div>
      <div>
        <FavoSiteList />
      </div>
    </div>
  );
};

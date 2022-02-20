import { useAppDispatch, useAppSelector } from "../app/hooks";
import { selectSiteListState, selectWord } from "../slices/siteSlice";
import { StarIcon } from "@heroicons/react/outline";

export const SiteList = () => {
  const selectSiteList = useAppSelector(selectSiteListState);
  const dispatch = useAppDispatch();
  const word = useAppSelector(selectWord);

  return (
    <>
      <div className="text-center">
        <h2 className="text-lg text-gray-900 mb-2">検索結果</h2>
        {selectSiteList.length === 0 ? (
          <span>検索結果がありません</span>
        ) : (
          <ul>
            {selectSiteList.map((site, index) => {
              return (
                <>
                  <li key={index}>
                    <a
                      href={site.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <span className="hover:text-gray-500 hover:underline">
                        {site.title}
                      </span>
                    </a>
                    <button>
                      <StarIcon
                        className="h-6 w-6 mr-3 ml-3 text-yellow-300 cursor-pointer hover:text-yellow-600"
                        // onClick={() =>
                        //   dispatch(
                        //     createFavoSite({
                        //       // user_id: user_id,
                        //       title: site.title,
                        //       url: site.url,
                        //       word: word,
                        //     })
                        //   )
                        // }
                      />
                    </button>
                  </li>
                </>
              );
            })}
          </ul>
        )}
      </div>
    </>
  );
};

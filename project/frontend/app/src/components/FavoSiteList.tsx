import { selectFavoSiteListState } from "../slices/siteSlice";
import { useAppSelector } from "../app/hooks";
import { StarIcon } from "@heroicons/react/solid";


export const FavoSiteList = () => {
  const selectFavoSiteList = useAppSelector(selectFavoSiteListState);

  return (
    <>
      <div className="text-center">
        <h2 className="text-lg text-gray-900 mb-2">お気に入り</h2>
        {selectFavoSiteList.length === 0 ? (
          <span>お気に入りがありません</span>
        ) : (
          <ul>
            {selectFavoSiteList.map((site) => {
              return (
                <li key={site.url}>
                  <a href={site.url}>
                    <span>{site.title}</span>
                  </a>
                  <button>
                    <StarIcon />
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </>
  );
};


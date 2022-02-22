import { StarIcon } from "@heroicons/react/solid";
import { useQueryFavoSite } from "../hooks/useQueryFavoSite";
import { useProcessSite } from "../hooks/useProcessSite";


export const FavoSiteList = () => {
  const { data: dataFavoSite, isLoading: isLoadingFavoSite } =
    useQueryFavoSite();
  const { processPutFavoSite } = useProcessSite();

  if (isLoadingFavoSite)
    return <span className="text-center text-lg text-gray-900">Loading</span>;
  
  return (
    <>
      <div className="text-center">
        <h2 className="text-lg text-gray-900 mb-2">お気に入り</h2>
        {dataFavoSite?.length === 0 ? (
          <span>お気に入りがありません</span>
        ) : (
          <ul>
            {dataFavoSite?.map((site) => {
              return (
                <>
                  <li key={site.site_id}>
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
                        onClick={() => processPutFavoSite(site.site_id)}
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

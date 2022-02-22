import { PostFavoSite } from "../types/SiteType";
import { useMutateSite } from "./useMutateSite";

export const useProcessSite = () => {
  const { createFavoSiteMutation, putFavoSiteMutation } = useMutateSite();

  const processFavoSite = (postSite: PostFavoSite) => {
    createFavoSiteMutation.mutate(postSite);
  };

  const processPutFavoSite = (site_id: string) => {
    putFavoSiteMutation.mutate(site_id);
  };

  return {
    processFavoSite,
    processPutFavoSite,
    createFavoSiteMutation,
    putFavoSiteMutation,
  };
};

export type PostFavoSite = {
  email: string
  title: string
  url: string
  word: string
};

export type SiteBase = {
  user_id: string;
  site_id: string
  title: string;
  url: string;
  word: string;
  is_deleted: number;
  version: number;
  created_at: string;
  updated_at: string;
};

export type PostSite = {
  title: string
  url: string
}
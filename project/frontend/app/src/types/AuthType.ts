export type CsrfToken = {
  csrf_token: string;
};

export type Credentials = {
  email: string;
  password: string;
};

export type UserInfo = {
  user_id: string
  username: string | null
  email: string
  password: string
  is_deleted: number;
  version: number;
  created_at: string;
  updated_at: string;
};

export type Email = {
  email: string
}
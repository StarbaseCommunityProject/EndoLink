export interface User {
  url: string;
  id: number;
  username: string;
  email: string;
  groups: string[];
  leading_faction: string | null;
  member_of_faction: string[];
}

export interface SignUpResponse {
  jwt: { refresh: string, access: string };
  user: User
}

export interface SignUpErrorResponse {
  status: number;
  message: string;
}

export interface LogInResponse {
  access: string;
  refresh: string;
}

export interface LogInErrorResponse {
  status: number;
  message: string;
}

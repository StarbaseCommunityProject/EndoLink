import { User } from './user.types';

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

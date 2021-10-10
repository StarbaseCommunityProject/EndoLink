export interface User {
  url: string;
  id: number;
  username: string;
  email: string;
  groups: string[];
  leading_faction: string | null;
  member_of_faction: string[];
}

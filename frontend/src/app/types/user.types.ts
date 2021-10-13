export interface User {
  url: string;
  id: number;
  username: string;
  email: string;
  groups: string[];
  leading_faction: string | null;
  member_of_faction: string[];
  profile_picture: string;
  extra_info: {
    in_game_name: string;
    discord_name: string;
    forum_name: string;
    bio: string;
    home_origin: null | string;
    profile_picture: string;
  }
}

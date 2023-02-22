export const authGuard = (to, from) => {
  const token = getCookie("X-Access-Token");
  if (!token) {
    return "/login";
  }
};

function getCookie(name: string) {
  const re = new RegExp(name + "=([^;]+)");
  const value = re.exec(document.cookie);
  return value != null ? unescape(value[1]) : null;
}

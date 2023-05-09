# leetcode 0929 - Unique Email Addresses
# Easy
#
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters,
# the email may contain one or more '.' or '+'.
#     For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
#
# If you add periods '.' between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# Note that this rule does not apply to domain names.
#     For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
#
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#     For example, "m.y+name@email.com" will be forwarded to "my@email.com".
#
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each emails[i],
# return the number of different addresses that actually receive mails.

# Time: O(m*n) Memory: O(n)
class BuiltInSolution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)


class ManualSolution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            i, local = 0, ""
            while email[i] not in ["@", "+"]:
                if email[i] != ".":
                    local += email[i]
                i += 1

            while email[i] != "@":
                i += 1
            domain = email[i + 1:]
            unique.add((local, domain))
        return len(unique)

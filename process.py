import csv
import uuid

from font import change_font

def fill_message_template(candidate_name, company_name, role, job_id, job_link, employee_name, resume_link):
    if job_id == '' and job_link == '':
        message_text = f"Hello {employee_name}, \n\nI am writing this message to seek a referral for the {role} role at {company_name}. " \
                       f"\n\nCould you please have a look at my resume in your free time and tell me if I am good enough for" \
                       f" the above-mentioned role, to earn a referral from you? \n\n𝗥𝗲𝘀𝘂𝗺𝗲 𝗟𝗶𝗻𝗸: {resume_link}\n\n" \
                       f"I respect and value and your time. You can also drop a '𝗡𝗼' and I won't bother you with a " \
                       f"follow-up message. 🙂\n\nRegards\n{candidate_name}"
    elif job_id == '':
        message_text = f"Hello {employee_name}, \n\nI am writing this message to seek a referral for the {role} role at {company_name}." \
                       f"\n\n𝗝𝗼𝗯 𝗟𝗶𝗻𝗸: {job_link}" \
                       f"\n\nCould you please have a look at my resume in your free time and tell me if I am good enough for" \
                       f" the above-mentioned role, to earn a referral from you? \n\n𝗥𝗲𝘀𝘂𝗺𝗲 𝗟𝗶𝗻𝗸: {resume_link}\n\n" \
                       f"I respect and value and your time. You can also drop a '𝗡𝗼' and I won't bother you with a " \
                       f"follow-up message. 🙂\n\nRegards\n{candidate_name}"
    elif job_link == '':
        message_text = f"Hello {employee_name}, \n\nI am writing this message to seek a referral for the {role} role at {company_name}." \
                       f"\n\n𝗝𝗼𝗯 𝗜𝗗: {job_id}" \
                       f"\n\nCould you please have a look at my resume in your free time and tell me if I am good enough for" \
                       f" the above-mentioned role, to earn a referral from you? \n\n𝗥𝗲𝘀𝘂𝗺𝗲 𝗟𝗶𝗻𝗸: {resume_link}\n\n" \
                       f"I respect and value and your time. You can also drop a '𝗡𝗼' and I won't bother you with a " \
                       f"follow-up message. 🙂\n\nRegards\n{candidate_name}"
    else:
        message_text = f"Hello {employee_name}, \n\nI am writing this message to seek a referral for the {role} role at {company_name}." \
                       f"\n\n𝗝𝗼𝗯 𝗜𝗗: {job_id}" \
                       f"\n\n𝗝𝗼𝗯 𝗟𝗶𝗻𝗸: {job_link}" \
                       f"\n\nCould you please have a look at my resume in your free time and tell me if I am good enough for" \
                       f" the above-mentioned role, to earn a referral from you? \n\n𝗥𝗲𝘀𝘂𝗺𝗲 𝗟𝗶𝗻𝗸: {resume_link}\n\n" \
                       f"I respect and value and your time. You can also drop a '𝗡𝗼' and I won't bother you with a " \
                       f"follow-up message. 🙂\n\nRegards\n{candidate_name}"
    return message_text

def generate_messages(file_path, candidate_name, resume_link):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        company_names, roles, job_ids, job_links, employee_names = zip(
            *((row[0], row[1], row[2], row[3], row[4]) for row in csv_reader))
        company_list = list(company_names[1:])
        role_list = list(roles[1:])
        job_id_list = list(job_ids[1:])
        job_link_list = list(job_links[1:])
        employee_list = list(employee_names[1:])
    csv_file.close()

    generated_file_name = f"Messages-{candidate_name}-{uuid.uuid4()}.txt"

    with open(generated_file_name, 'w') as f:
        for company_name, role, job_id, job_link, employee_name in zip(company_list, role_list, job_id_list,
                                                                       job_link_list, employee_list):
            company_name = change_font(company_name)
            role = change_font(role)
            print("===============================================================", file=f)
            print(f"Company Name: {company_name} | Employee Name: {employee_name}", file=f)
            print("===============================================================", file=f, end='\n\n')
            print(
                fill_message_template(candidate_name, company_name, role, job_id, job_link, employee_name, resume_link),
                file=f,
                end='\n\n'
            )
    f.close()

    return generated_file_name


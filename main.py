from member_operations import MemberOperations
from member import Member

if __name__ == '__main__':
    # Create an object of MemberOperations
	member_operations = MemberOperations()

    # create a connection to the db
	member_operations.connect()

    # get cursor object
	member_operations.get_cursor_object()

    # create table member
	member_operations.create_table()

    # Create initial members
	member1 = Member('Erick', 'Mwazonga', '0702345678')
	member2 = Member('Alex', 'Mwadondo', '0798235421')
	member3 = Member('Erick', 'Mbwana', '0789321546')
	member4 = Member('Keffa', 'Kithaka', '0798461200')
	member5 = Member('Eli', 'Mdedi', '0721627392')

	members = [
		(member1.account_number(), member1.firstname, member1.lastname, member1.telephone, member1.get_email(), member1.get_balance()),
		(member2.account_number(), member2.firstname, member2.lastname, member2.telephone, member2.get_email(), member2.get_balance()),
		(member3.account_number(), member3.firstname, member3.lastname, member3.telephone, member3.get_email(), member3.get_balance()),
		(member4.account_number(), member4.firstname, member4.lastname, member4.telephone, member4.get_email(), member4.get_balance()),
		(member5.account_number(), member5.firstname, member5.lastname, member5.telephone, member5.get_email(), member5.get_balance()),
	]

    # insert members
	member_operations.insert_many_members(members)

    # member1 deposit
	balance_after_deposit = member1.deposit(2000)

    # update balance after deposit by supplying ID
	member1_telephone = members[0][3]
	member_operations.update_balance(member1_telephone, balance_after_deposit)

	# member1 withdraw
	balance_after_withdraw = member1.withdraw(500)

	# update balance after withdrwa by supplying ID
	member1_telephone = members[0][3]
	member_operations.update_balance(member1_telephone, balance_after_withdraw)

	# search member by account number
	member_operations.search_member_by_account_number('YNWH2N88K35ZGGRFRHAY')

    # get all members
	member_operations.get_all_members()

    # close the connectionn
	member_operations.disconnect()

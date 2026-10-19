from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 3


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
# TODO 1: days_left is negative when the task is overdue.
def test_days_left_counts_days_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 10)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == -9

# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    #Act
    result = is_urgent(due, today)
    #Assert
    assert result == True

# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_two_days():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    #Act
    result = is_urgent(due, today)
    #Assert
    assert result == True

# TODO 4: is_urgent is False when the task is overdue.
def test_is_urgent_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    #Act
    result = is_urgent(due, today)
    #Assert
    assert result == False

# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due():
    # Arrange
    tasks = [
        {"title": "Final Year Project", "due": date(2026, 10, 21)},
        {"title": "Lab 2", "due": date(2026, 9, 15)},
        {"title": "Assignment 1", "due": date(2026, 8, 30)},
    ]
    # Act
    result = sort_by_due(tasks)
    # Assert
    assert result[0]["title"] == "Assignment 1"
    assert result[1]["title"] == "Lab 2"
    assert result[2]["title"] == "Final Year Project"

# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_when_no_task():
    # Arrange
    done = 0
    total = 0
    #Act
    result = completion_rate(done, total)
    #Assert
    assert result == 0.0

# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_when_had_task():
    # Arrange
    done = 1
    total = 3
    #Act
    result = completion_rate(done, total)
    #Assert
    assert result == 33.3
area = float(input('Enter area on one wall: '))
interior_cost = float(input('Enter cost of painting interior wall per sq.ft: '))
exterior_cost = float(input('Enter cost of painting exterior wall per sq.ft: '))

total_wall_area = area * 8
interior_total = total_wall_area * interior_cost
exterior_total = total_wall_area * exterior_cost

total_cost = interior_total + exterior_total

print('Total wall area =', total_wall_area, 'sq.ft')
print('Interior painting cost =', interior_total)
print('Exterior painting cost =', exterior_total)
print('Total painting cost =', total_cost)
/**
 * @name Avoid eval in application code
 * @description Finds calls to Python eval(), which can execute attacker-controlled expressions.
 * @kind problem
 * @problem.severity warning
 * @security-severity 7.5
 * @precision high
 * @id py/custom/avoid-eval
 */

import python

from Call call
where call.getTarget().hasName("eval")
select call, "Avoid eval(): it can execute attacker-controlled code."

import java.util.*;
import com.google.common.collect.ImmutableSet;
import com.google.template.soy.pysrc.restricted.SoyPySrcFunction;
import com.google.template.soy.pysrc.restricted.PyExpr;

/**
 * Provides a function for calling a python method dynamically.
 */
public class CallMethodFunction implements SoyPySrcFunction {

    public PyExpr computeForPySrc(List<PyExpr> args) {
        // Module and method
        String module = args.get(0).getText();
        String method = args.get(1).getText();
        // Create comma separated param string... "param1, param2"
        Integer size = args.size();
        StringBuilder params = new StringBuilder();
        for (Integer i = 2; i < args.size(); i++) {
            String value = args.get(i).getText();
            params.append(value);
            if (i < size - 1) {
                params.append(", ");
            }
        }
        // Create python import/call statement
        String code = String.format("getattr(__import__(%s), %s)(%s)", module, method, params);
        return new PyExpr(code, Integer.MAX_VALUE);
    }

    public String getName() {
        return "callMethod";
    }

    public Set<Integer> getValidArgsSizes() {
        // Minimum 2 args - module and method
        // Up to 15 param values
        return ImmutableSet.of(2, 3, 4, 5,
                6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17);
    }

}
